from fastapi import APIRouter, Depends, Query
from typing import List
from bson import ObjectId
from ..ai.recommendation_engine import RecommendationEngine
from .auth import get_current_user
from ..models.content import ContentOut

router = APIRouter()
engine = RecommendationEngine()

@router.get("/next", response_model=List[ContentOut])
async def next_content(
    limit: int = Query(5, ge=1, le=20),
    current=Depends(get_current_user)
):
    recs = await engine.recommend_for_user(str(current["_id"]), top_k=limit)
    # Map raw documents to ContentOut
    return [
        ContentOut(
            id=str(c["_id"]),
            title=c["title"],
            description=c["description"],
            content_type=c["content_type"],
            url=c.get("url"),
            metadata=c.get("metadata", {}),
            created_by=str(c["created_by"])
        )
        for c in recs
    ]