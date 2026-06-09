from pydantic import BaseModel

class RecipeCreate(BaseModel):
    title: str
    chef: str
    prep_time: int
    instructions: str

class Recipe(RecipeCreate):
    id: int