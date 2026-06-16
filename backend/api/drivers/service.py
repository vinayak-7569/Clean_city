from sqlalchemy.orm import Session

from backend.database.models.assignment import Assignment
from backend.database.models.complaint import Complaint
from backend.database.models.driver import Driver

from backend.api.notifications.service import (
    create_notification
)

def get_driver_by_user_id(
    db: Session,
    user_id: int
):
    return db.query(
        Driver
    ).filter(
        Driver.user_id == user_id
    ).first()


def get_driver_tasks(
    db: Session,
    driver_id: int
):
    return db.query(
        Assignment
    ).filter(
        Assignment.driver_id == driver_id
    ).all()


def get_task_details(
    db: Session,
    complaint_id: int
):
    return db.query(
        Complaint
    ).filter(
        Complaint.id == complaint_id
    ).first()


def update_task_status(
    db: Session,
    complaint_id: int,
    status: str
):

    complaint = db.query(
        Complaint
    ).filter(
        Complaint.id == complaint_id
    ).first()

    if complaint is None:
        return None

    complaint.status = status

    if status == "completed":

        create_notification(
            db=db,
            user_id=complaint.citizen_id,
            message="Your complaint has been marked as completed."
        )

    db.commit()

    db.refresh(complaint)

    return complaint