from ..config import db,auth,verify_token
from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv('FIREBASE_API_KEY')
def login_user(user_data):
    try:
        # Use Firebase Admin SDK to verify user credentials (email & password)
        user = auth.get_user_by_email(user_data.email)  # Get user by email
        
        # Verify the password (you may want to handle password checking with Firebase)
        # Unfortunately, Firebase Admin SDK doesn't support login directly, so use the REST API.
        url = f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}'
        payload = {
            "email": user_data.email,
            "password": user_data.password,
            "returnSecureToken": True
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an error if the request failed
        
        # If login is successful, Firebase returns the user data
        user_data = response.json()
        return {"message": "Login successful", "user": user_data}
    except Exception as e:
        return {"error": str(e)}

# Crear un nuevo usuario en Firestore
def create_user(user_data):
    try:
        # Extracting user data from the input

        # Create a new user in Firebase Authentication
        user_record = auth.create_user(
            email=user_data.email,
            password=user_data.password
        )

        # Save user details to Firestore
        user_ref = db.collection('User').document(user_record.uid)
        user_ref.set({
            "id_user": user_record.uid,
            'email': user_data.email,
            "name": user_data.name,
            "surname": user_data.surname,
            "weight": user_data.weight,
            "height": user_data.height,
            "birthDate": user_data.birthDate
        })

        return {"message": "User created and data saved successfully"}
    except Exception as e:
        return {"error": str(e)}

def get_user_by_email(email):
    try:
        users_ref = db.collection('User')
        query = users_ref.where('email', '==', email).stream()

        for user in query:
            return user.to_dict()  # If user is found, return user data as a dictionary
        
        return None  # Return None if no user is found
    except Exception as e:
        return {"error": str(e)}
def send_password_reset_email(email):
    # Firebase Auth REST API URL
    url = f'https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key={api_key}'

    # API Key is required here. Replace `YOUR_API_KEY` with your Firebase project's API key.
    payload = {
        'requestType': 'PASSWORD_RESET',
        'email': email
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors

        if response.json().get('email'):
            return {'message': 'Password reset email sent! Please check your inbox'}
        else:
            return {'message': 'Unexpected response from Firebase'}

    except requests.exceptions.HTTPError as err:
        return {'error': f'Error during password reset: {err}'}
    
def get_current_user_service(request):
    token = request.headers.get('Authorization').split("Bearer ")[1]
    decoded_token = verify_token(token)
    return decoded_token