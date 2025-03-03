from pydantic import BaseModel, constr

class PostBase(BaseModel):
    text: constr(max_length=1048576)  # 1MB limit

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True