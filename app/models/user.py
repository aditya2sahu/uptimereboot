from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    is_verified = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    user_profile = relationship("UserProfile",back_populates="user")


class UserProfile(Base):
    __tablename__ = "user_profile"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id', ondelete="CASCADE"),unique=True, index=True, nullable=False)
    subscription_id = Column(Integer, ForeignKey('subscription.id', ondelete="CASCADE"), nullable=True)
    name = Column(String, nullable=False)
    subscription = relationship("Subscription", back_populates="user_profile")
    user = relationship("User", back_populates="user_profile")
    monitor = relationship("Monitor", back_populates="monitor")
