from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database.session import get_db

from backend.api.auth.dependencies import (
    require_admin
)

from backend.api.forecasting.service import (
    generate_forecasts,
    get_forecasts
)

from backend.database.schemas.forecast_schema import (
    ForecastResponse
)

router = APIRouter(
    prefix="/forecasts",
    tags=["Forecasts"]
)


@router.post("/generate")
def generate(
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):

    return generate_forecasts(
        db=db
    )


@router.get(
    "",
    response_model=list[
        ForecastResponse
    ]
)
def forecasts(
    db: Session = Depends(get_db)
):

    return get_forecasts(
        db=db
    )