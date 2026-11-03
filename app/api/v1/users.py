from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from starlette import status

from app.core.security import pwd_context, create_access_token
from app.models.user import User, UserProfile
from app.db.session import SessionLocal, get_db
from app.schema import UserCreate, UserResponse, User as UserPydantic

user_router = APIRouter(
    tags=["users"],
    prefix="/api/v1",
)

@user_router.post("/auth/register/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, db:Session = Depends(get_db)):
    try:
        is_exists = db.query(User).filter(User.email == payload.email).first()

        if is_exists:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

        user = User(
            email = payload.email,
            password= pwd_context.hash(payload.password),
        )
        db.add(user)
        db.flush()

        user_profile = UserProfile(
            user_id= user.id,
            name=payload.name,
        )
        db.add(user_profile)
        token = create_access_token(user.id)
        try:
            db.commit()
        except Exception:
            db.rollback()

        return {
            "name":payload.name,
            "email":payload.email,
            "token":token,
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))



@user_router.get("/users/", response_model=List[UserPydantic])
def get_users(skip: int = 0, limit: int = 100, db:Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users