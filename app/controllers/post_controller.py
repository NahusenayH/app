from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.models.database import get_db
from app.schemas.post import Post, PostCreate
from app.services.post_service import PostService
from app.utils.auth import get_current_user

router = APIRouter()

@router.post("/posts", response_model=Post)
async def create_post(
    post: PostCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user)
):
    """
    Create a new post for the authenticated user
    """
    return await PostService.create_post(db, current_user, post)

@router.get("/posts", response_model=List[Post])
async def get_posts(
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user)
):
    """
    Retrieve all posts for the authenticated user
    """
    return await PostService.get_user_posts(db, current_user)

@router.delete("/posts/{post_id}")
async def delete_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user)
):
    """
    Delete a specific post by ID
    """
    await PostService.delete_post(db, post_id, current_user)
    return {"message": "Post deleted successfully"}