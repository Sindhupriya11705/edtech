from fastapi import APIRouter, HTTPException, Response, Request, Depends
from itsdangerous import TimestampSigner, BadSignature, SignatureExpired
from ..config import settings
from ..models.user import UserCreate, UserOut, UserLogin
from ..repositories.user_repo import (
    create_user, authenticate_user, get_user_by_id, get_user_by_email
)

router = APIRouter()
signer = TimestampSigner(settings.SECRET_KEY)
SESSION_COOKIE = "edtech_session"

@router.post("/register", response_model=UserOut)
async def register(user: UserCreate):
    if await get_user_by_email(user.email):
        raise HTTPException(400, "Email already registered")
    created = await create_user(user)
    return UserOut(
        id=str(created["_id"]),
        email=created["email"],
        role=created["role"],
        name=created["name"]
    )

@router.post("/login")
async def login(user: UserLogin, response: Response):
    db_user = await authenticate_user(user.email, user.password)
    if not db_user:
        raise HTTPException(400, "Invalid credentials")
    # Sign and set session cookie
    token = signer.sign(str(db_user["_id"]).encode()).decode()
    response.set_cookie(
        key=SESSION_COOKIE,
        value=token,
        httponly=True,
        max_age=7*24*3600,  # 1 week
        samesite="lax"
    )
    return {"message": "Logged in successfully"}

@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie(SESSION_COOKIE)
    return {"message": "Logged out"}

# Dependency to get current user
async def get_current_user(request: Request):
    token = request.cookies.get(SESSION_COOKIE)
    if not token:
        raise HTTPException(401, "Not authenticated")
    try:
        unsigned = signer.unsign(token, max_age=7*24*3600)
        user_id = unsigned.decode()
    except (BadSignature, SignatureExpired):
        raise HTTPException(401, "Invalid or expired session")
    user = await get_user_by_id(user_id)
    if not user:
        raise HTTPException(401, "User not found")
    return user