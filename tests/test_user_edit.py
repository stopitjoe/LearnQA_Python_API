import time

import allure
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


@allure.epic("Testing user edit")
class TestUserEdit(BaseCase):

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test user edit - register, login, edit")
    def test_user_edit_create_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, 'id')

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login/", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_name = "Changed name"
        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_status_code(response3, 200)

        # GET
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_json_value_by_name(response4, "firstName", new_name, "Wrong user_name after edit")

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test user edit unauthorized")
    def test_user_edit_unauthorized(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response_register = MyRequests.post("/user/", data=register_data)

        Assertions.assert_status_code(response_register, 200)
        Assertions.assert_json_has_key(response_register, "id")

        user_id = self.get_json_value(response_register, 'id')

        # EDIT
        new_name = "Changed name"
        response_edit = MyRequests.put(
            f"/user/{user_id}",
            data={"firstName": new_name}
        )

        Assertions.assert_status_code(response_edit, 400)
        assert response_edit.text == "Auth token not supplied", "Response text is not correct"

        # GET
        response_get = MyRequests.get(
            f"/user/{user_id}",
        )

        Assertions.assert_status_code(response_get, 200)
        Assertions.assert_json_value_by_name(response_get, "username", "learnqa", "Wrong user_name")

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test user edit - authorized another user")
    def test_user_edit_auth_another_user(self):
        # REGISTER USER 1
        register_data_user1 = self.prepare_registration_data()
        response_register_user1 = MyRequests.post("/user/", data=register_data_user1)

        Assertions.assert_status_code(response_register_user1, 200)
        Assertions.assert_json_has_key(response_register_user1, "id")

        email_user1 = register_data_user1['email']
        password_user1 = register_data_user1['password']

        # REGISTER USER 2
        time.sleep(2)
        register_data_user2 = self.prepare_registration_data()
        response_register_user2 = MyRequests.post("/user/", data=register_data_user2)

        Assertions.assert_status_code(response_register_user2, 200)
        Assertions.assert_json_has_key(response_register_user2, "id")

        user2_id = self.get_json_value(response_register_user2, 'id')

        # LOGIN USER 1
        login_data = {
            'email': email_user1,
            'password': password_user1
        }
        response_login = MyRequests.post("/user/login/", data=login_data)

        auth_sid = self.get_cookie(response_login, "auth_sid")
        token = self.get_header(response_login, "x-csrf-token")

        # EDIT USER 2
        new_name = "Changed name"
        response_edit = MyRequests.put(
            f"/user/{user2_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"username": new_name}
        )

        Assertions.assert_status_code(response_edit, 200)

        # GET
        response_get = MyRequests.get(
            f"/user/{user2_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_json_value_by_name(response_get, "username", "learnqa", "Wrong user_name")

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test user edit - invalid email")
    def test_user_edit_invalid_email(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response_register = MyRequests.post("/user/", data=register_data)

        Assertions.assert_status_code(response_register, 200)
        Assertions.assert_json_has_key(response_register, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response_register, 'id')

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response_login = MyRequests.post("/user/login/", data=login_data)

        auth_sid = self.get_cookie(response_login, "auth_sid")
        token = self.get_header(response_login, "x-csrf-token")

        # EDIT
        response_edit = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"email": "thisemail.com"}
        )

        Assertions.assert_status_code(response_edit, 400)
        assert response_edit.text == "Invalid email format", "Wrong response text from server"

        # GET
        response_get = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_status_code(response_get, 200)
        Assertions.assert_json_value_by_name(response_get, "email", f"{email}", "Email is not correct")

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test user edit - register, login, edit")
    def test_user_edit_short_firstName(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response_register = MyRequests.post("/user/", data=register_data)

        Assertions.assert_status_code(response_register, 200)
        Assertions.assert_json_has_key(response_register, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response_register, 'id')

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response_login = MyRequests.post("/user/login/", data=login_data)

        auth_sid = self.get_cookie(response_login, "auth_sid")
        token = self.get_header(response_login, "x-csrf-token")

        # EDIT
        new_name = "C"
        response_edit = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_status_code(response_edit, 400)
        Assertions.assert_json_value_by_name(response_edit, "error", "Too short value for field firstName", "text of response is not correct")

        # GET
        response_get = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_json_value_by_name(response_get, "firstName", "learnqa", "Wrong user_name after unsuccess edit")