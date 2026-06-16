from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database.session import get_db

from backend.api.auth.dependencies import (
    require_admin
)

from backend.api.routes.service import (
    generate_routes,
    get_routes
)

from backend.database.schemas.route_schema import (
    RouteResponse
)

router = APIRouter(
    prefix="/routes",
    tags=["Routes"]
)


@router.post("/generate")
def generate(
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):

    return generate_routes(
        db=db
    )


@router.get(
    "",
    response_model=list[
        RouteResponse
    ]
)
def routes(
    db: Session = Depends(get_db)
):

    return get_routes(
        db=db
    )