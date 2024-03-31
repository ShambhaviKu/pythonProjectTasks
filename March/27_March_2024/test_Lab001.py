import pytest
import requests
import allure

from conftest import create_booking, create_token

@allure.testcase("TC#1 update first name")
@allure.description("CRUD Operations")
@allure.title("PUT Request")
def test_put_request(create_token, create_booking):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"

    param = create_booking

    PUT_URL = base_url + base_path + str(param)

    cookie = "token=" + create_token

    HEADERS = {"content-type": "application/json",
               "Cookie": cookie
               }
    PAYLOAD = {
        "firstname": "lily",
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