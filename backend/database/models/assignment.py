from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from datetime import datetime

from backend.database.base import Base


class Assignment(Base):

    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True)

    complaint_id = Column(
        Integer,
        ForeignKey("complaints.id")
    )

    driver_id = Column(
        Integer,
        ForeignKey("drivers.id")
    )

    assigned_at = Column(
        DateTime,
        default=datetime.utcnow
    )