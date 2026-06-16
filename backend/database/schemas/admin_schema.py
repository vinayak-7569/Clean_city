from pydantic import BaseModel


class AssignDriverRequest(BaseModel):
    complaint_id: int
    driver_id: int


class UpdateStatusRequest(BaseModel):
    complaint_id: int
    status: str
class VerifyComplaintRequest(BaseModel):
    complaint_id: int