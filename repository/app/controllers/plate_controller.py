from app.service.plate_service import create_plate,get_user_plates,delete_Plate_service,update_Plate
from app.models.plate import Plate
from fastapi import HTTPException
from datetime import datetime


def plateLog(plate: Plate):
    response = create_plate(plate)
    if "error" in response:
        raise HTTPException(status_code=500, detail=response["error"])
    return {"message": "User Plate registered successfully"}
def get_plate_user(user_id: str):
    response = get_user_plates(user_id)
    if "error" in response:
        raise HTTPException(status_code=500, detail=response["error"])
    return {"message": response}


def delete_plate(userPlate_id: str):
    response = delete_Plate_service(userPlate_id)
    if "error" in response:
        raise HTTPException(status_code=500, detail=response["error"])


def update_plate_controller(userPlate_id: str, Plate_data: Plate):
    response = update_Plate(userPlate_id, Plate_data)
    if "error" in response:
        raise HTTPException(status_code=500, detail=response["error"])
    return {"message": response}
