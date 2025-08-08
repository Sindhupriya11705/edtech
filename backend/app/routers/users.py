from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..database import db
from ..models.user import UserOut
from ..repositories.user_repo import get_user_by_id, get_user_by_email
from .auth import get_current_user

router=APIRouter()

@router.get("/me", response_model=UserOut)
async def read_own_profile(current=Depends(get_current_user)):
    return UserOut(
        id=str(current["_id"]),
        email=current["email"],
        role=current["role"],
        name=current["name"]
    )

@router.get("/", response_model=List[UserOut])
async def list_users(current=Depends(get_current_user)):
    if current["role"] != "admin":
        raise HTTPException(403, "Admin privileges required")
    users = await db.users.find().to_list(length=1000)
    return [
        UserOut(
            id=str(u["_id"]),
            email=u["email"],
            role=u["role"],
            name=u["name"],
        )
        for u in users
    ]
