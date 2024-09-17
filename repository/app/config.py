import firebase_admin
from firebase_admin import credentials, firestore, auth
from fastapi import HTTPException

# Ensure Firebase is initialized only once
if not firebase_admin._apps:
    cred = credentials.Certificate("../serviceAccountKey.json")
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

