from pydantic import BaseModel
from typing import List, Optional


class IngredientSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class CategorySchema(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        from_attributes = True


class RecipeSchema(BaseModel):
    id: int
    title: str
    description: str
    cooking_steps: str
    cooking_time: int
    image: Optional[str] = None
    author_id: int
    created_at: str
    updated_at: str
    categories: List[CategorySchema] = []
    ingredients: List[IngredientSchema] = []

    class Config:
        from_attributes = True