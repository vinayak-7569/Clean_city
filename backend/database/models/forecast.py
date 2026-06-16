from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from backend.database.base import Base


class Forecast(Base):

    __tablename__ = "forecasts"

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

    current_complaints = Column(
        Integer
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