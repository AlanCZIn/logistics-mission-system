from sqlalchemy import Column, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum


class MissionStatus(str, enum.Enum):
    PENDING = "PENDING"
    ASSIGNED = "ASSIGNED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"


class Mission(Base):
    __tablename__ = "missions"

    id = Column(Integer, primary_key=True)
    status = Column(Enum(MissionStatus), default=MissionStatus.PENDING)
    assigned_user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    assigned_user = relationship("User")