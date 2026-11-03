from starlette import status

from .conftest import client


def test_register_user(client):
    data = {
        "email": "test@gmail.com",
        "password": "12345678",
        "name": "aadi",
    }
    response = client.post("/api/v1/auth/register/", json=data)
    print(response)
    assert response.status_code == status.HTTP_201_CREATED

if __name__ == "__main__":
    test_register_user(client)