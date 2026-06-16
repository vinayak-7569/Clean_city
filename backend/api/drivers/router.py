from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from backend.database.session import get_db

from backend.database.models.user import User

from backend.api.auth.dependencies import (
    require_driver
)

from backend.api.drivers.service import (
    get_driver_tasks,
    get_task_details,
    update_task_status,
    get_driver_by_user_id
)

from backend.database.schemas.driver_schema import (
    TaskStatusUpdate
)

router = APIRouter(
    prefix="/driver",
    tags=["Driver"]
)


@router.get("/tasks")
def tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_driver
    )
):

    driver = get_driver_by_user_id(
        db=db,
        user_id=current_user.id
    )

    if driver is None:
        raise HTTPException(
            status_code=404,
            detail="Driver profile not found"
        )

    return get_driver_tasks(
        db=db,
        driver_id=driver.id
    )


@router.get("/tasks/{complaint_id}")
def task_details(
    complaint_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_driver
    )
):

    complaint = get_task_details(
        db=db,
        complaint_id=complaint_id
    )

    if complaint is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    return complaint


@router.patch("/tasks")
def update_status(
    request: TaskStatusUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_driver
    )
):

    complaint = update_task_status(
        db=db,
        complaint_id=request.complaint_id,
        status=request.status
    )

    if complaint is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    return complaint