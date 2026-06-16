from pydantic import BaseModel
from datetime import datetime


class RouteResponse(BaseModel):

    id: int

    stop_number: int

    latitude: float

    longitude: float

    predicted_complaints: int

    predicted_risk: str

    created_at: datetime

    model_config = {
        "from_attributes": True
    }