from fastapi import APIRouter,Depends,Request
from app.models.food import Food
from app.controllers.food_controller import register_new_food, get_foods, get_food_by_id
from app.controllers.category_controller import userCategoryLog,get_category,update_category_controller,delete_category
from app.controllers.catFood_controller import CategoryFoodLog,get_Food_perCat,delete_Catfood
# from app.models.user import UserRegister, UserForgotPassword, UserLogin
# from app.controllers.user_controller import 
from app.models.catFood import CategoryFood
from app.models.category import Category
from app.models.userFood import UserFood
from app.controllers.foodUser_controller import userFoodLog,get_meals_user,delete_meal
from datetime import datetime
from .config import verify_token


router = APIRouter()

# Define a simple root endpoint
@router.get("/")
def read_main():
    return {"msg": "Server is running"}

@router.post("/Food_log/")
async def register_food(Food: Food):
    # user_id = verify_token(token)
    # if not user_id:
    #      raise HTTPException(status_code=403, detail="Invalid token")
    register_new_food(Food)
    return {"message": "Food log added!"}

@router.get("/Foods/")
async def read_food_logs():
    return get_foods()
@router.get("/Foods/{food_id}")
async def get_food(food_id: str):
    return get_food_by_id(food_id)

async def get_current_user(request: Request):
    token = request.headers.get('Authorization').split("Bearer ")[1]
    decoded_token = await verify_token(token)
    return decoded_token

@router.get("/api/user")
async def get_user_data(current_user: dict = Depends(get_current_user)):
    # Now you have access to the current user
    return {"email": current_user["email"], "uid": current_user["uid"]}



@router.post("/UserFood_log/")
async def register_foodMeal(FoodUser: UserFood):
    userFoodLog(FoodUser)
    return {"message": "Meal log added!"}

@router.get("/mealUserDay/{user_id}")
async def get_meal(user_id:str):
    return get_meals_user(user_id)

@router.delete("/DeleteMealUser/{id_UserFood}")
async def delete_mealUser(id_UserFood:str):
    return delete_meal(id_UserFood)

@router.post("/CreateCategory/")
async def category_log(category: Category):
    userCategoryLog(category)
    return {"message": "new category!"}

@router.get("/GetCategoryUser/{user_id}")
async def get_category_user(user_id:str):
    return get_category(user_id)
@router.put("/UpdateCategroy/{category_id}")
async def update_category(category_id:str,updated_category: Category):
    return update_category_controller(category_id,updated_category)

@router.post("/CreateCatFood/")
async def category_log(catFood: CategoryFood):
    CategoryFoodLog(catFood)
    return {"message": "new categoryFood!"}
@router.get("/GetFoodsPerCategory/{id_Category}")
async def get_Food_Percategory(id_Category:str):
    return get_Food_perCat(id_Category)

@router.delete("/DeleteCategory/{id_Category}")
async def delete_category_user(id_Category:str):
    delete_category(id_Category)
    delete_Catfood(id_Category)
    return {"message": "new categoryFood!"}




