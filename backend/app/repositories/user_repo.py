from typing import Optional
from bson import ObjectId
from passlib.context import CryptContext
from ..database import db
from ..models.user import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def get_user_by_email(email: str) -> Optional[dict]:
    return await db.users.find_one({"email": email})

async def get_user_by_id(user_id: str) -> Optional[dict]:
    return await db.users.find_one({"_id": ObjectId(user_id)})

async def create_user(user: UserCreate) -> dict:
    hashed = pwd_context.hash(user.password)
    user_dict = user.dict()
    user_dict["hashed_password"] = hashed
    del user_dict["password"]
    result = await db.users.insert_one(user_dict)
    return await get_user_by_id(str(result.inserted_id))

async def authenticate_user(email: str, password: str) -> Optional[dict]:
    user = await get_user_by_email(email)
    if not user:
        return None
    if not pwd_context.verify(password, user["hashed_password"]):
        return None
    return user