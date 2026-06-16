from pydantic import BaseModel
from datetime import datetime


class ForecastResponse(BaseModel):

    id: int

    latitude: float

    longitude: float

    current_complaints: int

    predicted_complaints: int

    predicted_risk: str

    created_at: datetime

    model_config = {
        "from_attributes": True
    }