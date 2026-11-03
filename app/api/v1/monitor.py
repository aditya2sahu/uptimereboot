from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.dependancies import get_current_user
from db.session import get_db
from models import UserProfile
from models.monitor import Monitor
from schema import *


monitor_router = APIRouter(prefix="/api/v1", tags=["monitor"])

@monitor_router.get("/add/monitor", response_model=CommonResponse)
def add_monitor(user: get_current_user ,payload:MonitorCreate,db:Session = Depends(get_db()),):
    try:

        user_profile = db.query(UserProfile).filter(user=user).first()

        if not user_profile:
            raise HTTPException(status_code=404, detail="User does not exist")

        monitor = Monitor(
            user_profile = user_profile,
            name=payload.name,
            url=payload.url,
            data =payload.data,
            expected_status= payload.expected_status,
            timeout= payload.timeout,
            interval_seconds = payload.interval_seconds,
            headers = payload.headers,
            method = payload.method
        )
        db.add(monitor)
        db.commit()
        return {
            "status": True,
            "message": "Monitor added successfully",
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


