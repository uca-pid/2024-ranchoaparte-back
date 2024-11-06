import firebase_admin
from firebase_admin import credentials, firestore, auth
from fastapi import HTTPException
import os
import json
from dotenv import load_dotenv

load_dotenv()


# Ensure Firebase is initialized only once
if not firebase_admin._apps:
    firebase_cred_json = os.getenv('FIREBASECREDENTIALS')
    firebase_creds_dict= json.loads(firebase_cred_json)

    cred = credentials.Certificate(firebase_creds_dict)
    firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()

# Authentication (Admin SDK does not use 'getAuth' like the JS SDK)
auth = firebase_admin.auth
async def verify_token(token: str):
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")
def migrate_plates_to_add_verified():
    plates_ref = db.collection("User")
    plates = plates_ref.stream()

    for plate in plates:
        plate_data = plate.to_dict()
        
        # Check if `verified` field is missing
        if 'validation' not in plate_data:
            print(f"Updating plate {plate.id} to add 'verified' field.")
            plates_ref.document(plate.id).update({"validation": ""})  # Set default value
            
    print("Migration completed for all plates.")

# Run the migration
migrate_plates_to_add_verified()

