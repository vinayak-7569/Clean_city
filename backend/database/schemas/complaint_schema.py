from pydantic import BaseModel
from datetime import datetime


class ComplaintCreate(BaseModel):
    title: str
    description: str
    latitude: float
    longitude: float
    image_url: str | None = None
    waste_category: str


class ComplaintResponse(BaseModel):
    id: int
    title: str
    description: str
    latitude: float
    longitude: float
    image_url: str | None
    status: str
    citizen_id: int
    created_at: datetime
    waste_category: str
    priority: str

    model_config = {
        "from_attributes": True
    }