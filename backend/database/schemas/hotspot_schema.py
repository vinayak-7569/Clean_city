from pydantic import BaseModel
from datetime import datetime


class HotspotResponse(BaseModel):

    id: int

    latitude: float

    longitude: float

    complaint_count: int

    average_severity: float

    risk_level: str

    created_at: datetime

    model_config = {
        "from_attributes": True
    }