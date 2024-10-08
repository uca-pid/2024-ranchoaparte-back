from pydantic import BaseModel, Field
from typing import List

class Plate(BaseModel):
    id_User: str
    name : str
    ingredients_id: List[str]
    calories_portion: int

