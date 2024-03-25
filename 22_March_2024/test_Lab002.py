import pytest
import requests   # pip install requests

import allure
@allure.title("Test Authgentication")
@allure.description("get request")
@allure.tag("NewUI", "essentials")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "shambhavi")
@allure.testcase("TCId = 123")
@allure.issue("AUTH=123")

@pytest.mark.smoke
def test_get_single_request_by_id():
    Request = requests.get("https://restful-booker.herokuapp.com/booking/2")
    print(Request.json())
    print(Request.text)
    print(Request.cookies)
    print(Request.headers)
    print(Request.url)
    response_code = Request.status_code
    assert response_code == 200