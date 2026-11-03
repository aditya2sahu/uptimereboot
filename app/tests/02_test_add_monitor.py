import json
from .conftest import client


def test_create_monitor(client):
    data = {
        "name": "Google",
        "url": "https://google.com",
        "data":None,
        "expected_status": 200,
        "timeout": 10,
        "interval_seconds": 300,
        "headers" : {
            "Content-Type": "application/json"
        },
        "method": "GET",
    }
    response = client.post("/api/v1/add/monitor",body=json.dumps(data), headers={"Content-Type": "application/json"})
    print(response.json())
    assert response.status_code == 200



if __name__ == "__main__":
   test_create_monitor()