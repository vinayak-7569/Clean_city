from sqlalchemy.orm import Session

from backend.database.models.complaint import Complaint
from backend.database.models.ai_result import AIResult

from backend.database.schemas.complaint_schema import (
    ComplaintCreate
)


def calculate_priority(
    waste_category: str,
    description: str
):

    description = description.lower()

    severity_score = 5.0
    priority = "Medium"

    if waste_category == "Construction Waste":
        severity_score = 9.0
        priority = "Critical"

    elif waste_category == "E-Waste":
        severity_score = 8.0
        priority = "High"

    elif waste_category == "Mixed Waste":
        severity_score = 7.0
        priority = "High"

    if (
        "road" in description
        or "traffic" in description
        or "blocked" in description
    ):
        severity_score += 1

    severity_score = min(
        severity_score,
        10.0
    )

    return severity_score, priority


def create_complaint(
    db: Session,
    complaint: ComplaintCreate,
    citizen_id: int
):

    severity_score, priority = (
        calculate_priority(
            complaint.waste_category,
            complaint.description
        )
    )

    new_complaint = Complaint(
        title=complaint.title,
        description=complaint.description,
        latitude=complaint.latitude,
        longitude=complaint.longitude,
        image_url=complaint.image_url,
        citizen_id=citizen_id,
        waste_category=complaint.waste_category,
        priority=priority
    )

    db.add(new_complaint)

    db.commit()

    db.refresh(new_complaint)

    ai_result = AIResult(
        complaint_id=new_complaint.id,
        user_category=complaint.waste_category,
        ai_category=complaint.waste_category,
        confidence=0.90,
        severity_score=severity_score,
        priority=priority
    )

    db.add(ai_result)

    db.commit()

    return new_complaint


def get_my_complaints(
    db: Session,
    citizen_id: int
):

    return db.query(
        Complaint
    ).filter(
        Complaint.citizen_id == citizen_id
    ).all()


def get_complaint_by_id(
    db: Session,
    complaint_id: int
):

    return db.query(
        Complaint
    ).filter(
        Complaint.id == complaint_id
    ).first()