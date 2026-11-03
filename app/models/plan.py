from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, String, Float, JSON

from app.db.base import Base


class Plan(Base):
    __tablename__ = "plan"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    details = Column(JSON, nullable=False)

    subscription = relationship("Subscription", back_populates="plan")