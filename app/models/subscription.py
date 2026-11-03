from app.db.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey, Float, DateTime


class Subscription(Base):
    __tablename__ = "subscription"

    id = Column(Integer, primary_key=True)
    plan_id = Column(Integer,ForeignKey("plan.id", ondelete="SET NULL"),nullable=True)
    plan_name = Column(String, nullable=False)
    plan_amount = Column(Float, nullable=True)
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)

    plan = relationship("Plan", back_populates="subscription",)
    user_profile = relationship("UserProfile", back_populates="subscription",)