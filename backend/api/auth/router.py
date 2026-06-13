from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from backend.database.session import get_db

from backend.database.schemas.user_schema import (
    UserCreate,
    UserResponse
)

from backend.database.schemas.auth_schema import (
    LoginRequest,
    TokenResponse
)

from backend.api.auth.service import (
    create_user,
    login_user
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse
)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    return create_user(
        db=db,
        user=user
    )


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    return login_user(
        db=db,
        email=request.email,
        password=request.password
    )