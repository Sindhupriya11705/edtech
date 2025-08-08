
from bson import ObjectId
from ..database import db
from .nlp_utils.embedding_service import embed_text
import numpy as np

class RecommendationEngine:
    async def recommend_for_user(self, user_id: str, top_k: int = 5) -> list[dict]:
        # 1. Fetch user history of content interactions
        user = await db.users.find_one({"_id": ObjectId(user_id)})
        history_ids: list[str] = user.get("history", [])

        # 2. Build user profile embedding
        embeddings = []
        for cid in history_ids:
            content = await db.content.find_one({"_id": ObjectId(cid)})
            if content:
                text = f"{content['title']} {content['description']}"
                embeddings.append(embed_text(text))
        if embeddings:
            user_emb = np.mean(np.vstack(embeddings), axis=0)
        else:
            # Cold-start: zero vector
            user_emb = np.zeros((384,))

        # 3. Score all content by cosine similarity
        all_contents = await db.content.find().to_list(length=None)
        scored = []
        for c in all_contents:
            text = f"{c['title']} {c['description']}"
            c_emb = embed_text(text)
            score = float(np.dot(user_emb, c_emb))
            scored.append((score, c))

        # 4. Sort & filter out already seen
        scored.sort(key=lambda x: x[0], reverse=True)
        recommendations = [c for score, c in scored if str(c["_id"]) not in history_ids]

        # 5. Return top_k
        return recommendations[:top_k]