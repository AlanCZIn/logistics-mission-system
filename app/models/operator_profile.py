from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class OperatorProfile(Base):
    __tablename__ = "operator_profiles"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    capacity_limit = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)

    user = relationship("User")