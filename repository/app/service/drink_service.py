from ..config import db
from datetime import datetime, timedelta

def create_drink(drink_data):
    try:
        new_drink_ref = db.collection('Drink').document()
        new_drink_ref.set(drink_data)
        return {"message": "drink added successfully", "id": new_drink_ref.id}
    except Exception as e:
        return {"error": str(e)}
def drinks(user_id):
    try:
        user_drinks_query = db.collection(
            'Drink').where('id_User', '==', user_id)
        user_drinks = user_drinks_query.stream()

        drinks_list = []
        for drinks in user_drinks:
            drinks_dict = drinks.to_dict()
            drinks_dict['id'] = drinks.id
            drinks_list.append(drinks_dict)
        return {"message": "List fetched successfully", "Drinks": drinks_list}
    except Exception as e:
        return {"error": str(e)}
def drink_by_id(drink_id):
    try:
        # Referencia al documento del drinko
        drink_ref = db.collection('Drink').document(drink_id)
        drink_doc =drink_ref.get()
        return {"drink": drink_doc.to_dict(), "message": "drink get successful"}
    except Exception as e:
        return {"error": str(e)}
def delete_drink(drink_id):
    try:
        # Referencia al documento del foodo
        food_ref = db.collection('Drink').document(drink_id)
        food_ref.delete()
        return {"message": "user drink  delete successful"}
    except Exception as e:
        return {"error": str(e)}
def update_Drink(userDrink_id, Drink_data):
    try:
        updated_data = Drink_data.dict()
        Drink_ref = db.collection('Drink').document(userDrink_id)
        Drink_ref.update(updated_data)

        return {"message": "Drink updated successfully"}
    except Exception as e:
        return {"error": str(e)}