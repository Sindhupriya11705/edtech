from pydantic import BaseModel, Field, HttpUrl
from enum import Enum
from bson import ObjectId
from .user import PyObjectId

class ContentType(str, Enum):
    video    = "video"
    article  = "article"
    quiz     = "quiz"

class ContentInDB(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str
    description: str
    content_type: ContentType
    url: HttpUrl | None = None        # for video/article
    metadata: dict = {}               # e.g. tags, difficulty
    created_by: PyObjectId            # teacher/admin who created it

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}

class ContentCreate(BaseModel):
    title: str
    description: str
    content_type: ContentType
    url: HttpUrl | None = None
    metadata: dict = {}

class ContentUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    url: HttpUrl | None = None
    metadata: dict | None = None

class ContentOut(BaseModel):
    id: str
    title: str
    description: str
    content_type: ContentType
    url: HttpUrl | None
    metadata: dict
    created_by: str