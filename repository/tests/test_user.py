import pytest
from repository.app import app
# Importa tu aplicación Flask


@pytest.fixture
def client():
    app.config['TESTING'] = True  # Habilita el modo de pruebas
    with app.test_client() as client:
        yield client


def test_create_user(client):
    # Simular los datos que se van a enviar para crear un usuario
    user_data = {
        "email": "test@example.com",
        "password": "test123",
        "name": "Test",
        "surname": "User",
        "weight": 70,
        "height": 170,
        "birthDate": "1990-01-01"
    }

    response = client.post('/create_user', json=user_data)
    assert response.status_code == 200
    assert b"User created and data saved successfully" in response.data
