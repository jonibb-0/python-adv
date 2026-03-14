from pydantic import BaseModel

class CategoryBase(BaseModel):
    id: int
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int

class Category(CategoryBase):
    id: int