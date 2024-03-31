import pytest
import requests
import allure


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

@allure.testcase("TC#1 update first name")
@allure.description("CRUD Operations")
@allure.title("PUT Request")
def test_put_request():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"

    param = create_booking()

    PUT_URL = base_url + base_path + str(param)

    cookie = "token=" + create_token()

    HEADERS = {"content-type": "application/json",
               "Cookie": cookie
               }
    PAYLOAD = {
        "firstname": "ram",
        "lastname": "wite",
        "totalprice": 153,
        "depositpaid": "false",
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-01"
        },
        "additionalneeds": "lunch"
    }

    response = requests.put(url=PUT_URL, headers=HEADERS, json=PAYLOAD)
    assert response.status_code == 200

    response_body = response.json()
    assert response.json()

    first_name = response_body["firstname"]
    assert first_name == "lily", "Failed Message - Incorrect FirstName"
    assert type(first_name) == str
    assert first_name is not None


def test_delete_request():
    try:
        URL = "https://restful-booker.herokuapp.com/booking/"
        booking_id = create_booking()
        DELETE_URL = URL + str(booking_id)
        cookie_value = "token=" + create_token()
        headers = {
            "Content-Type": "application/json",
            "Cookie": cookie_value
        }
        print(headers)

        response = requests.delete(url=DELETE_URL, headers=headers)
        # Assertions
        assert response.status_code == 201
    except Exception as e:
        print(e)
