from pydantic import BaseModel, Field
from typing import List

class Drink(BaseModel):
    name : str
    amount_sugar: int
    amount_cafeine: int 
    calories_portion: int
    measure_portion: int
    measure: str
    typeOfDrink: str
    id_User: str
