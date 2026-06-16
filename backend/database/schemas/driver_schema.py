from pydantic import BaseModel


class TaskStatusUpdate(BaseModel):
    complaint_id: int
    status: str