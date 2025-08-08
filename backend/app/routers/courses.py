

from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List

from ..models.content import ContentOut, ContentCreate, ContentUpdate
from ..repositories.content_repo import (
    list_content,
    get_content,
    create_content,
    update_content,
    delete_content,
)
from .auth import get_current_user

router = APIRouter()


@router.get("/", response_model=List[ContentOut])
async def read_courses(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1),
    current=Depends(get_current_user),
):
    items = await list_content(skip=skip, limit=limit)
    return [
        ContentOut(
            id=str(i["_id"]),
            title=i["title"],
            description=i["description"],
            content_type=i["content_type"],
            url=i.get("url"),
            metadata=i.get("metadata", {}),
            created_by=str(i["created_by"]),
        )
        for i in items
    ]


@router.get("/{content_id}", response_model=ContentOut)
async def read_course(content_id: str, current=Depends(get_current_user)):
    item = await get_content(content_id)
    if not item:
        raise HTTPException(404, "Content not found")
    return ContentOut(
        id=str(item["_id"]),
        title=item["title"],
        description=item["description"],
        content_type=item["content_type"],
        url=item.get("url"),
        metadata=item.get("metadata", {}),
        created_by=str(item["created_by"]),
    )


@router.post("/", response_model=ContentOut)
async def create_course(
    data: ContentCreate, current=Depends(get_current_user)
):
    if current["role"] not in ("teacher", "admin"):
        raise HTTPException(403, "Only teachers/admins may create content")
    created = await create_content(data, str(current["_id"]))
    return ContentOut(
        id=str(created["_id"]),
        title=created["title"],
        description=created["description"],
        content_type=created["content_type"],
        url=created.get("url"),
        metadata=created.get("metadata", {}),
        created_by=str(created["created_by"]),
    )


@router.put("/{content_id}", response_model=ContentOut)
async def update_course(
    content_id: str, data: ContentUpdate, current=Depends(get_current_user)
):
    existing = await get_content(content_id)
    if not existing:
        raise HTTPException(404, "Content not found")
    if current["role"] != "admin" and str(existing["created_by"]) != str(current["_id"]):
        raise HTTPException(403, "Not authorized to modify this content")
    updated = await update_content(content_id, data)
    return ContentOut(
        id=str(updated["_id"]),
        title=updated["title"],
        description=updated["description"],
        content_type=updated["content_type"],
        url=updated.get("url"),
        metadata=updated.get("metadata", {}),
        created_by=str(updated["created_by"]),
    )


@router.delete("/{content_id}")
async def delete_course(content_id: str, current=Depends(get_current_user)):
    existing = await get_content(content_id)
    if not existing:
        raise HTTPException(404, "Content not found")
    if current["role"] != "admin" and str(existing["created_by"]) != str(current["_id"]):
        raise HTTPException(403, "Not authorized to delete this content")
    success = await delete_content(content_id)
    if not success:
        raise HTTPException(500, "Failed to delete")
    return {"message": "Content deleted"}