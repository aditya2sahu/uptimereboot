from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    created_at = Column(DateTime, server_default=func.now())
    is_deleted = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)