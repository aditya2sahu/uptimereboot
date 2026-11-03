from app.db.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, JSON


class Monitor(Base):
    __tablename__ = 'monitor'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    url = Column(String, nullable=False)
    data = Column(JSON, nullable=False)
    expected_status =  Column(Integer, nullable=False)
    timeout = Column(Integer, nullable=False)
    is_active = Column(Integer, nullable=False)
    interval_seconds = Column(Integer, default=300)
    headers = Column(JSON, nullable=False)
    method = Column(String, nullable=False, default='GET')

    user_profile = relationship("UserProfile", back_populates="monitor")
    check_log = relationship("CheckLog", back_populates="monitor")



