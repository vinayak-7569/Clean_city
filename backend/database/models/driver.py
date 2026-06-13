from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from backend.database.base import Base


class Driver(Base):

    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    phone = Column(String)

    vehicle_number = Column(String)