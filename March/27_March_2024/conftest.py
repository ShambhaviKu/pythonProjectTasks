import pytest
import requests

@pytest.fixture()
def create_token():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/auth"
    URL = base_url + base_path

    HEADER = {"content-type": "application/json"}
    PAYLOAD = {
        "username": "admin",
        "password": "password123"
    }

    Response = requests.post(url=URL, headers=HEADER, json=PAYLOAD)
    Response_body = Response.json()
    token = Response_body["token"]
    print(token)
    return token

@pytest.fixture()
def create_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path

    HEADER = {"content-type": "application/json"}
    PAYLOAD = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": "true",
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    Response = requests.post(url=URL, headers=HEADER, json=PAYLOAD)

    assert Response.status_code == 200  # validation
    Response_body = Response.json()
    Booking_id = Response_body["bookingid"]
    print(Booking_id)

    return Booking_id
