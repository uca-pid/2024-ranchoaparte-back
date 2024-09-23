from ..config import db

def createUserTotCal_service(userTotCal):
    
    try:
        totCal_data_dict = userTotCal.dict()
        new_totCal = db.collection('UserTotalCal').document()
        new_totCal.set(totCal_data_dict)
        return {"message": "New Total added successfully", "id": new_totCal.id}
    except Exception as e:
        return {"error": str(e)}


def updateDailyCalories(calPerDay_id, dataUpdate):
    try:
        updated_data = dataUpdate.dict()
        usertotCal_ref = db.collection('UserTotalCal').document(calPerDay_id)
        usertotCal_ref.update(updated_data)

        return {"message": "UserTotalCal updated successfully"}
    except Exception as e:
        return {"error": str(e)}
def get_totalCAL(user_id):
    try:
        user_TotCal_query = db.collection(
            'UserTotalCal').where('id_user', '==', user_id)
        user_totCal = user_TotCal_query.stream()
        
        totCal_list = []
        for totCal in user_totCal:
            totCal_dict = totCal.to_dict()
            print(totCal_dict)
            totCal_dict['id'] = totCal.id
            totCal_list.append(totCal_dict)
        sorted_totCal_list = sorted(totCal_list, key=lambda x: x['day'])
        return {"message": "List fetched successfully", "totCals": totCal_list}
    except Exception as e:
        return {"error": str(e)}

    


