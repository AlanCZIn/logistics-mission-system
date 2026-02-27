from sqlalchemy import Column, Integer, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base
from app.models.mission import MissionStatus


class MissionHistory(Base):
    __tablename__ = "mission_history"

    id = Column(Integer, primary_key=True)
    mission_id = Column(Integer, ForeignKey("missions.id"))
    previous_status = Column(Enum(MissionStatus))
    new_status = Column(Enum(MissionStatus))

    previous_operator_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    new_operator_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    changed_at = Column(DateTime, default=datetime.utcnow)

    mission = relationship("Mission")