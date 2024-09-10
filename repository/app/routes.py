from fastapi import APIRouter
from app.models.food import Food
from app.controllers.food_controller import register_new_food, get_foods, get_food_by_id

router = APIRouter()

# Define a simple root endpoint
@router.get("/")
def read_main():
    return {"msg": "Server is running"}

@router.post("/Food_log/")
async def register_food(Food: Food):
    # user_id = verify_token(token)
    # if not user_id:
    #     raise HTTPException(status_code=403, detail="Invalid token")
    register_new_food(Food)
    return {"message": "Food log added!"}

@router.get("/Foods/")
async def read_food_logs():
    # user_id = verify_token(token)
    # if not user_id:
    #     raise HTTPException(status_code=403, detail="Invalid token")

    # logs = get_Foods(user_id)
    return get_foods()
@router.get("/Foods/{food_id}")
async def get_food(food_id: str):
    return get_food_by_id(food_id)

