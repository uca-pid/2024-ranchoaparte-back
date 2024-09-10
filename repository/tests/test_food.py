from fastapi import FastAPI
from fastapi.testclient import TestClient


app = FastAPI()

# Define a simple root endpoint
@app.get("/")
def read_main():
    return {"msg": "Server is running"}



client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Server is running"}


# # Use pytest's fixture to create the test client
# @pytest.fixture
# def anyio_backend():
#     return 'asyncio'

# @pytest.mark.anyio
# async def test_food_by_id_success():
#     # Create a test client using FastAPI
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         print(ac)
#         response = await ac.get("/Food/uF1fgcv8BswFmUgUI5aX")  # Replace with a valid food_id in your Firestore

#     # Assert that the request was successful
#     assert response.status_code == 200
#     data = response.json()
    
#     # Check the response content
#     assert "food" in data
#     assert data["message"] == "food get successful"


# @pytest.mark.anyio
# async def test_food_by_id_not_found():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.get("/Food/nonexistent-id")

#     assert response.status_code == 200  # You can adjust the status code if needed
#     data = response.json()

#     # Check the error response
#     assert "error" in data
