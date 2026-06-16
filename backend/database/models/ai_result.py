from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime

from datetime import datetime

from backend.database.base import Base


class AIResult(Base):

    __tablename__ = "ai_results"

    id = Column(
        Integer,
        primary_key=True
    )

    complaint_id = Column(
        Integer,
        ForeignKey("complaints.id")
    )

    user_category = Column(
        String
    )

    ai_category = Column(
        String
    )

    confidence = Column(
        Float
    )

    severity_score = Column(
        Float
    )

    priority = Column(
        String
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )