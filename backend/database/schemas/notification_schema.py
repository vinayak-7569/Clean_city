from pydantic import BaseModel
from datetime import datetime


class NotificationResponse(BaseModel):

    id: int
    user_id: int
    message: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }