from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database.session import get_db

from backend.api.admin.service import (
    get_all_complaints,
    assign_driver,
    update_complaint_status,
    verify_complaint
)

from backend.api.auth.dependencies import (
    require_admin
)

from backend.database.schemas.admin_schema import (
    AssignDriverRequest,
    UpdateStatusRequest,
    VerifyComplaintRequest
)

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/complaints")
def all_complaints(
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):

    return get_all_complaints(db)


@router.post("/assign-driver")
def assign(
    request: AssignDriverRequest,
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):

    return assign_driver(
        db=db,
        complaint_id=request.complaint_id,
        driver_id=request.driver_id
    )


@router.patch("/status")
def update_status(
    request: UpdateStatusRequest,
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):

    return update_complaint_status(
        db=db,
        complaint_id=request.complaint_id,
        status=request.status
    )
@router.post("/verify")
def verify(
    request: VerifyComplaintRequest,
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):

    return verify_complaint(
        db=db,
        complaint_id=request.complaint_id
    )