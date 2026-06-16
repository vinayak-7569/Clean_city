from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from backend.database.base import Base


class Hotspot(Base):

    __tablename__ = "hotspots"

    id = Column(
        Integer,
        primary_key=True
    )

    latitude = Column(
        Float
    )

    longitude = Column(
        Float
    )

    complaint_count = Column(
        Integer
    )

    average_severity = Column(
        Float
    )

    risk_level = Column(
        String
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )