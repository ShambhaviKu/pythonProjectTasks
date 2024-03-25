import pytest

import requests

import allure


def create_token():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/auth"
    URL = base_url + base_path

    HEADERS = {"content-type": "application/json"}

    DATA = {
        "username": "admin",
        "password": "password123"
    }

    response_data = requests.post(url=URL, headers=HEADERS, json=DATA)
    payload_data = response_data.json()
    token = payload_data["token"]
    return token


def create_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path

    HEADERS = {"content-type": "application/json"}

    DATA = {
        "firstname": "john",
        "lastname": "carry",
        "totalprice": 596,
        "depositpaid": "true",
        "bookingdates": {
            "checkin": "2024-05-10",
            "checkout": "2024-05-12"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=URL, headers=HEADERS, json=DATA)
    payload_data = response.json()
    booking_id = payload_data["bookingid"]
    print(booking_id)
    return booking_id


@allure.description("CRUD OPERATION")
@allure.testcase("TC#5 update data")
@allure.tag("CRUD OPERATION", "Update data")
def test_update_firstname_positive():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"
    param = create_booking()

    PUT_URL = base_url + base_path + str(param)

    COOKIE = "token=" + create_token()

    HEADER = {"Content-Type": "application/json",
              "Cookie": COOKIE}

    payload = {"firstname": "lily",
               "lastname": "jerrye",
               "totalprice": 1000,
               "depositpaid": "true",
               "bookingdates": {
                   "checkin": "2024-05-10",
                   "checkout": "2024-05-12"
               },
               "additionalneeds": "Breakfast"
               }

    response = requests.put(url=PUT_URL, json=payload, headers=HEADER)
    response_data = response.json()

    # response_data validation

    first_name = response_data["firstname"]
    assert first_name == "lily", "error msg = Incorrect Name"
    assert type(first_name) == str
    assert (first_name) is not None

    last_name = response_data["lastname"]
    assert last_name == "jerrye"
    assert type(last_name) == str

    total_price = response_data["totalprice"]
    assert total_price > 0
    assert total_price == 1000
    assert type(total_price) == int


@allure.description("CRUD OPERATION")
@allure.testcase("TC#6 Delete data")
@allure.tag("CRUD OPERATION", "Delete data")
def test_delele_booking_id():
    try:

        base_url = "https://restful-booker.herokuapp.com"
        base_path = "/booking/"
        param = create_booking()

        DELET_URL = base_url + base_path + str(param)

        cookie = "token=" + create_token()

        HEADER = {"content-type":"application/json",
                  "cookie": cookie}

        response = requests.delete(url=DELET_URL, headers=HEADER)

        assert response.status_code == 201

        print(param)
    except Exception as e:
        print(e)

