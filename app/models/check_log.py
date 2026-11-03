from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, JSON

from db.base import Base


class CheckLog(Base):
    __tablename__ = "check_log"

    id = Column(Integer, primary_key=True, autoincrement=True)
    monitor_id = Column(Integer, ForeignKey("monitor.id", ondelete="CASCADE"))
    expected_status_code = Column(Integer, nullable=False)
    received_status_code = Column(Integer, nullable=False)
    received_message = Column(String, nullable=False)
    data = Column(JSON, nullable=False)
    message = Column(String, nullable=False)

    monitor = relationship("Monitor", back_populates="check_log")

