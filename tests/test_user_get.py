import allure

from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


@allure.epic("User get cases")
class TestUserGet(BaseCase):
    @allure.description("User get - not authorized")
    def test_user_get_not_auth(self):
        response = MyRequests.get('/user/2')
        unexpected_keys = ["email", "firstName", "lastName"]

        Assertions.assert_json_has_key(response, 'username')
        Assertions.assert_json_has_not_keys(response, unexpected_keys)

    @allure.description("User get - authorized the same user")
    def test_user_get_auth_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post('/user/login', data=data)

        auth_sid = self.get_cookie(response1, 'auth_sid')
        token = self.get_header(response1, 'x-csrf-token')
        user_id_from_auth = self.get_json_value(response1, 'user_id')

        response2 = MyRequests.get(f"/user/{user_id_from_auth}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid})

        expected_keys = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response2, expected_keys)

    @allure.description("User get - authorized another user")
    def test_user_get_auth_another_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        login_response = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(login_response, 'auth_sid')
        token = self.get_header(login_response, 'x-csrf-token')

        get_response = MyRequests.get("/user/1",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid})
        expected_keys = 'username'
        unexpected_keys = ["email", "firstName", "lastName"]

        Assertions.assert_json_has_key(get_response, expected_keys)
        Assertions.assert_json_has_not_keys(get_response, unexpected_keys)
