from ..config import db

def create_drinkType(drinkType_data):
    try:
        new_drinkType_ref = db.collection('DrinkType').document()
        new_drinkType_ref.set(drinkType_data)
        return {"message": "drinkType added successfully", "id": new_drinkType_ref.id}
    except Exception as e:
        return {"error": str(e)}
def drinkType():
    try:
        drinkType_ref = db.collection('DrinkType')
        drinkType = drinkType_ref.stream()
        drinkType_list = []

        for drinkType in drinkType:
            drinkType_dict = drinkType.to_dict()
            drinkType_dict['id'] = drinkType.id
            drinkType_list.append(drinkType_dict)
            
        return {"drinkType": drinkType_list, "message": "drinkType get successful"}
    except Exception as e:
        return {"error": str(e)}, 500
def drinkType_by_id(drinkType_id):
    try:
        # Referencia al documento del drinkTypeo
        drinkType_ref = db.collection('DrinkType').document(drinkType_id)
        drinkType_doc =drinkType_ref.get()
        return {"drinkType": drinkType_doc.to_dict(), "message": "drinkType get successful"}
    except Exception as e:
        return {"error": str(e)}