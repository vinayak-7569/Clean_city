from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database.session import get_db

from backend.database.models.user import User

from backend.api.auth.dependencies import (
    get_current_user
)

from backend.api.notifications.service import (
    get_user_notifications
)

from backend.database.schemas.notification_schema import (
    NotificationResponse
)

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


@router.get(
    "",
    response_model=list[NotificationResponse]
)
def my_notifications(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    return get_user_notifications(
        db=db,
        user_id=current_user.id
    )