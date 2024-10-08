from ..config import db
from datetime import datetime, timedelta

def create_drink(drink_data):
    try:
        new_drink_ref = db.collection('Drink').document()
        new_drink_ref.set(drink_data)
        return {"message": "drink added successfully", "id": new_drink_ref.id}
    except Exception as e:
        return {"error": str(e)}
def drinks():
    try:
        drink_ref = db.collection('Drink')
        drink = drink_ref.stream()
        drink_list = []

        for drink in drink:
            drink_dict = drink.to_dict()
            drink_dict['id'] = drink.id
            drink_list.append(drink_dict)
            
        return {"drink": drink_list, "message": "drink get successful"}
    except Exception as e:
        return {"error": str(e)}, 500
def drink_by_id(drink_id):
    try:
        # Referencia al documento del drinko
        drink_ref = db.collection('Drink').document(drink_id)
        drink_doc =drink_ref.get()
        return {"drink": drink_doc.to_dict(), "message": "drink get successful"}
    except Exception as e:
        return {"error": str(e)}