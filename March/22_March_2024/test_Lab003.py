import pytest
import requests

import allure


@allure.description("CRUD Operation")
@allure.testcase("TC#3 CREATE Booking")
@allure.tag("CRUD", "CRETE Booking")
@pytest.mark.e2e
def test_create_booking_by_id_positive():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path

    HEADERS = {"content-type": "application/json"}

    DATA = {
        "firstname": "rosesh",
        "lastname": "singh",
        "totalprice": 123,
        "depositpaid": "true",
        "bookingdates": {
            "checkin": "2024-03-10",
            "checkout": "2024-03-12"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=URL, headers=HEADERS, json=DATA)

    # Response

    response_code = response.status_code
    assert response_code == 200

    print(response.headers)

    # validate response body

    response_body = response.json()
    booking_id = response_body["bookingid"]
    print(booking_id)
    assert booking_id is not None
    assert booking_id > 0
    assert type(booking_id) == int

    booking_name = response_body["booking"]["firstname"]
    print(booking_name)
    assert booking_name is not None
    assert booking_name == "rosesh"
    assert type(booking_name) == str

    count = 0
    for i in booking_name:
        if i == "r":
            count = count + 1

    assert count > 0


@allure.description("CRUD Operation")
@allure.testcase("TC#4 CREATE Booking Negative")
@allure.tag("CRUD", "CRETE Booking")
@pytest.mark.e2e2
def test_create_booking_by_id_negative():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path

    HEADERS = {"content-type": "application/json"}

    DATA = { }

    response = requests.post(url=URL, headers=HEADERS, json=DATA)

    # Response

    response_code = response.status_code
    assert response_code == 500

    print(response.headers)



