from pydantic import BaseModel, Field
from typing import List

class PlateFood(BaseModel):
    ingredientId : str
    quantity: float = Field(..., ge=0)

class Plate(BaseModel):
    id_User: str
    name : str
    ingredients: List[PlateFood]
    calories_portion: float
    image: str

