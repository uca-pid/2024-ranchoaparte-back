
from ..config import db

def create_review(review_data):

    review_data_dict = review_data.dict()
    new_review_ref = db.collection('Review').document()
    new_review_ref.set(review_data_dict)

    return new_review_ref.id
def get_plate_reviews():
    
    try:
        plate_ref = db.collection('Review')
        plate = plate_ref.stream()
        plate_list = []

        for plate in plate:
            plate_dict = plate.to_dict()
            plate_dict['id'] = plate.id
            plate_list.append(plate_dict)
            
        return plate_list
    except Exception as e:
        return {"error": str(e)}, 500

def update_Review(review_id, review_data):
    try:
        updated_data = review_data.dict()
        Plate_ref = db.collection('Review').document(review_id)
        Plate_ref.update(updated_data)

        return "Review updated successfully"
    except Exception as e:
        return {"error": str(e)}

    
