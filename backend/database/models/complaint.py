from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from datetime import datetime

from backend.database.base import Base


class Complaint(Base):

    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    description = Column(String)

    latitude = Column(Float)

    longitude = Column(Float)

    image_url = Column(String)

    status = Column(String, default="pending")

    citizen_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    waste_category = Column(
        String,
        default="Mixed Waste"
    )

    priority = Column(
        String,
        default="Medium"
    )