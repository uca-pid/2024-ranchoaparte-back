from ..config import db

def create_plateFood(plateFood_data):
    try:
        # Convert the Pydantic model to a dictionary
        plateFood_data_dict = plateFood_data.dict()

        # Add the document to Firestore
        new_plateFood_ref = db.collection('PlateFood').document()
        new_plateFood_ref.set(plateFood_data_dict)

        return {"message": "plateFood added successfully to user", "id": new_plateFood_ref.id}
    except Exception as e:
        return {"error": str(e)}
    
# def get_user_plateFoods(id_user):
#     try:
#         user_plateFoods_query = db.collection(
#             'plateFood').where('id_User', '==', id_user)
#         user_plateFoods = user_plateFoods_query.stream()

#         plateFood_list = []
#         for plateFood in user_plateFoods:
#             plateFood_dict = plateFood.to_dict()
#             plateFood_dict['id'] = plateFood.id
#             plateFood_list.append(plateFood_dict)
#         return {"message": "List fetched successfully", "plateFoods": plateFood_list}
#     except Exception as e:
#         return {"error": str(e)}


def delete_plateFood_service(userplateFood_id):
    try:
        # Referencia al documento del plateFoodo
        plateFood_ref = db.collection('PlateFood').document(userplateFood_id)
        plateFood_ref.delete()
        return {"message": "user plateFood  delete successful"}
    except Exception as e:
        return {"error": str(e)}


def update_plateFood(userplateFood_id, plateFood_data):
    try:
        updated_data = plateFood_data.dict()
        plateFood_ref = db.collection('PlateFood').document(userplateFood_id)
        plateFood_ref.update(updated_data)

        return {"message": "plateFood updated successfully"}
    except Exception as e:
        return {"error": str(e)}
