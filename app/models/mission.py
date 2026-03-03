from sqlalchemy import Column, Integer, Enum as SqlEnum, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.domains.enums import MissionStatus


class Mission(Base):
    __tablename__ = "missions"

    id = Column(Integer, primary_key=True)
    status = Column(SqlEnum(MissionStatus), default=MissionStatus.PENDING)
    assigned_user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    assigned_user = relationship("User")