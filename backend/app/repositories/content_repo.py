from typing import Optional, List
from bson import ObjectId
from ..database import db
from ..models.content import ContentCreate, ContentUpdate

async def list_content(skip: int = 0, limit: int = 50) -> List[dict]:
    cursor = db.content.find().skip(skip).limit(limit)
    return await cursor.to_list(length=limit)

async def get_content(content_id: str) -> Optional[dict]:
    return await db.content.find_one({"_id": ObjectId(content_id)})

async def create_content(data: ContentCreate, creator_id: str) -> dict:
    # 1. Convert Pydantic model → plain dict
    payload = data.dict()

    # 2. Convert Enum to its value
    payload["content_type"] = payload["content_type"].value

    # 3. Convert HttpUrl (and any URL type) to str
    if payload.get("url") is not None:
        payload["url"] = str(payload["url"])

    # 4. Attach creator
    payload["created_by"] = ObjectId(creator_id)

    # 5. Insert and return
    result = await db.content.insert_one(payload)
    return await get_content(str(result.inserted_id))

async def update_content(content_id: str, data: ContentUpdate) -> Optional[dict]:
    update_data = {}
    for k, v in data.dict().items():
        if v is None:
            continue
        # same conversions for updated fields:
        if k == "content_type":
            update_data[k] = v.value
        elif k == "url":
            update_data[k] = str(v)
        else:
            update_data[k] = v

    if update_data:
        await db.content.update_one(
            {"_id": ObjectId(content_id)},
            {"$set": update_data}
        )
    return await get_content(content_id)

async def delete_content(content_id: str) -> bool:
    res = await db.content.delete_one({"_id": ObjectId(content_id)})
    return res.deleted_count == 1