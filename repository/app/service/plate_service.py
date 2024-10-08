from ..config import db
from datetime import datetime, timedelta

def create_plate(plate_data):
    try:
        # Convert the Pydantic model to a dictionary
        plate_data_dict = plate_data.dict()

        # Add the document to Firestore
        new_Plate_ref = db.collection('Plate').document()
        new_Plate_ref.set(plate_data_dict)

        return {"message": "Plate added successfully to user", "id": new_Plate_ref.id}
    except Exception as e:
        return {"error": str(e)}
    
def get_user_plates(id_user):
    try:
        user_Plates_query = db.collection(
            'Plate').where('id_User', '==', id_user)
        user_Plates = user_Plates_query.stream()

        Plate_list = []
        for Plate in user_Plates:
            Plate_dict = Plate.to_dict()
            Plate_dict['id'] = Plate.id
            Plate_list.append(Plate_dict)
        return {"message": "List fetched successfully", "Plates": Plate_list}
    except Exception as e:
        return {"error": str(e)}


def delete_Plate_service(userPlate_id):
    try:
        # Referencia al documento del Plateo
        plate_ref = db.collection('Plate').document(userPlate_id)
        plate_ref.delete()
        return {"message": "user Plate  delete successful"}
    except Exception as e:
        return {"error": str(e)}


def update_Plate(userPlate_id, plate_data):
    try:
        updated_data = plate_data.dict()
        Plate_ref = db.collection('Plate').document(userPlate_id)
        Plate_ref.update(updated_data)

        return {"message": "Plate updated successfully"}
    except Exception as e:
        return {"error": str(e)}
