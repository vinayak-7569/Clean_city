from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from backend.database.base import Base


class Route(Base):

    __tablename__ = "routes"

    id = Column(
        Integer,
        primary_key=True
    )

    stop_number = Column(
        Integer
    )

    latitude = Column(
        Float
    )

    longitude = Column(
        Float
    )

    predicted_complaints = Column(
        Integer
    )

    predicted_risk = Column(
        String
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )