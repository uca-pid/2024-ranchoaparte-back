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
def migrate_user_verified_to_int():
    users_ref = db.collection("Plate")
    users = users_ref.stream()

    for user in users:
        user_data = user.to_dict()
        
        # Check if `verified` field exists and is of type str
        if 'verified' in user_data and isinstance(user_data['verified'], str):
            try:
                # Attempt to convert `verified` from str to int
                new_verified = int(user_data['verified'])
            except ValueError:
                # If conversion fails, set a default value (e.g., 0)
                new_verified = 0
            
            # Update the `verified` field with the new integer value
            users_ref.document(user.id).update({"verified": new_verified})
            print(f"Updated user {user.id} verified to integer: {new_verified}")
        elif 'verified' not in user_data:
            # If `verified` field is missing, set a default integer value
            users_ref.document(user.id).update({"verified": 0})
            print(f"Added verified field for user {user.id} with default value: 0")
    
    print("Migration completed for all users.")

# Run the migration
migrate_user_verified_to_int()


