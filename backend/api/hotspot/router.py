from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database.session import get_db

from backend.api.auth.dependencies import (
    require_admin
)

from backend.api.hotspot.service import (
    generate_hotspots,
    get_hotspots
)

from backend.database.schemas.hotspot_schema import (
    HotspotResponse
)

router = APIRouter(
    prefix="/hotspots",
    tags=["Hotspots"]
)


@router.post(
    "/generate"
)
def generate(
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):

    return generate_hotspots(
        db=db
    )


@router.get(
    "",
    response_model=list[
        HotspotResponse
    ]
)
def hotspots(
    db: Session = Depends(get_db)
):

    return get_hotspots(
        db=db
    )