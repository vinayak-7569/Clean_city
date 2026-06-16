from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)

from sqlalchemy.orm import Session

from backend.database.session import get_db
from backend.database.models.user import User

from backend.core.jwt_handler import decode_token


security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    token = credentials.credentials

    payload = decode_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user_id = payload.get("user_id")

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user
def require_admin(
    current_user: User = Depends(
        get_current_user
    )
):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return current_user


def require_driver(
    current_user: User = Depends(
        get_current_user
    )
):
    if current_user.role != "driver":
        raise HTTPException(
            status_code=403,
            detail="Driver access required"
        )

    return current_user


def require_citizen(
    current_user: User = Depends(
        get_current_user
    )
):
    if current_user.role != "citizen":
        raise HTTPException(
            status_code=403,
            detail="Citizen access required"
        )

    return current_user