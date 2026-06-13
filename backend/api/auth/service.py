from sqlalchemy.orm import Session

from backend.database.models.user import User

from backend.database.schemas.user_schema import (
    UserCreate
)

from backend.core.security import (
    hash_password,
    verify_password
)

from backend.core.jwt_handler import (
    create_access_token
)


def create_user(
    db: Session,
    user: UserCreate
):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise Exception(
            "Email already registered"
        )

    new_user = User(
        name=user.name,
        email=user.email,
        password_hash=hash_password(
            user.password
        ),
        role=user.role
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return new_user


def login_user(
    db: Session,
    email: str,
    password: str
):

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        raise Exception(
            "Invalid email"
        )

    if not verify_password(
        password,
        user.password_hash
    ):
        raise Exception(
            "Invalid password"
        )

    token = create_access_token(
        {
            "user_id": user.id,
            "email": user.email,
            "role": user.role
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }