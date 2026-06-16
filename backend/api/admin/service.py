from sqlalchemy.orm import Session

from backend.database.models.complaint import Complaint
from backend.database.models.assignment import Assignment
from fastapi import HTTPException

from backend.api.notifications.service import (
    create_notification
)
def get_all_complaints(
    db: Session
):
    return db.query(
        Complaint
    ).all()


def assign_driver(
    db: Session,
    complaint_id: int,
    driver_id: int
):

    assignment = Assignment(
        complaint_id=complaint_id,
        driver_id=driver_id
    )

    db.add(assignment)

    complaint = db.query(
        Complaint
    ).filter(
        Complaint.id == complaint_id
    ).first()

    complaint.status = "assigned"

    create_notification(
        db=db,
        user_id=complaint.citizen_id,
        message="Your complaint has been assigned to a driver."
    )

    db.commit()

    db.refresh(assignment)

    return assignment


def update_complaint_status(
    db: Session,
    complaint_id: int,
    status: str
):

    complaint = db.query(
        Complaint
    ).filter(
        Complaint.id == complaint_id
    ).first()

    complaint.status = status

    db.commit()

    db.refresh(complaint)

    return complaint

def verify_complaint(
    db: Session,
    complaint_id: int
):

    complaint = db.query(
        Complaint
    ).filter(
        Complaint.id == complaint_id
    ).first()

    if complaint is None:
        return None

    if complaint.status != "completed":
        raise HTTPException(
        status_code=400,
        detail="Complaint must be completed before verification"
    )

    complaint.status = "resolved"

    create_notification(
        db=db,
        user_id=complaint.citizen_id,
        message="Your complaint has been resolved successfully."
    )

    db.commit()

    db.refresh(complaint)

    return complaint