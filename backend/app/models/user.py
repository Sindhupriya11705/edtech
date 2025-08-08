from pydantic import BaseModel, EmailStr, Field
from enum import Enum
from bson import ObjectId

# Helper to allow ObjectId fields in Pydantic
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

# Roles
class Role(str, Enum):
    student = "student"
    teacher = "teacher"
    admin   = "admin"

# Full DB record
class UserInDB(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    email: EmailStr
    hashed_password: str
    role: Role
    name: str
    # Tracking fields
    preferences: dict = {}
    history: list    = []
    scores: dict     = {}

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}

# Payload for registration
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: Role
    name: str

# Public output
class UserOut(BaseModel):
    id:    str
    email: EmailStr
    role:  Role
    name:  str
    class Config:
        allow_population_by_field_name = True
        allow_population_by_alias      = True


# Login payload
class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        allow_population_by_field_name = True
        allow_population_by_alias      = True