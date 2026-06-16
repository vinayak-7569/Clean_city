from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from backend.database.session import get_db

from backend.database.models.user import User

from backend.api.auth.dependencies import (
    require_citizen
)

from backend.api.complaints.service import (
    create_complaint,
    get_my_complaints,
    get_complaint_by_id
)

from backend.database.schemas.complaint_schema import (
    ComplaintCreate,
    ComplaintResponse
)

router = APIRouter(
    prefix="/complaints",
    tags=["Complaints"]
)


@router.post(
    "",
    response_model=ComplaintResponse
)
def create_new_complaint(
    complaint: ComplaintCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_citizen
    )
):

    return create_complaint(
        db=db,
        complaint=complaint,
        citizen_id=current_user.id
    )


@router.get(
    "/my",
    response_model=list[ComplaintResponse]
)
def my_complaints(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_citizen
    )
):

    return get_my_complaints(
        db=db,
        citizen_id=current_user.id
    )


@router.get(
    "/{complaint_id}",
    response_model=ComplaintResponse
)
def complaint_details(
    complaint_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_citizen
    )
):

    complaint = get_complaint_by_id(
        db=db,
        complaint_id=complaint_id
    )

    if complaint is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    return complaint