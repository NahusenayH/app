from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import List
from app.models.post import Post
from app.schemas.post import PostCreate
from app.utils.cache import cache
from app.config import settings

class PostService:
    @staticmethod
    async def create_post(db: Session, user_id: int, post: PostCreate) -> Post:
        db_post = Post(text=post.text, user_id=user_id)
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        cache.delete(f"user_posts_{user_id}")
        return db_post

    @staticmethod
    async def get_user_posts(db: Session, user_id: int) -> List[Post]:
        cache_key = f"user_posts_{user_id}"
        cached_posts = cache.get(cache_key)
        if cached_posts is not None:
            return cached_posts

        posts = db.query(Post).filter(Post.user_id == user_id).all()
        cache.set(cache_key, posts, settings.CACHE_EXPIRATION)
        return posts

    @staticmethod
    async def delete_post(db: Session, post_id: int, user_id: int) -> None:
        post = db.query(Post).filter(Post.id == post_id).first()
        if not post:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Post not found"
            )
        if post.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized to delete this post"
            )
            
        db.delete(post)
        db.commit()
        cache.delete(f"user_posts_{user_id}")