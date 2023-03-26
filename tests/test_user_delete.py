import allure
import time
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


@allure.epic("Test user delete")
class TestUserDelete(BaseCase):

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test user delete - try delete undeletable user")
    def test_delete_undeletable_user(self):

        # LOGIN
        login_data = {
            'email': "vinkotov@example.com",
            'password': "1234"
        }
        response_login = MyRequests.post("/user/login/", data=login_data)

        auth_sid = self.get_cookie(response_login, "auth_sid")
        token = self.get_header(response_login, "x-csrf-token")
        user_id = self.get_json_value(response_login, "user_id")

        # DELETE
        response_delete = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_status_code(response_delete, 400)
        assert response_delete.text == "Please, do not delete test users with ID 1, 2, 3, 4 or 5."

        # GET
        response_get = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_status_code(response_get, 200)
        Assertions.assert_json_value_by_name(response_get, "id", f"{user_id}", "Wrong user_id")

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test user delete")
    def test_user_delete(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response_register = MyRequests.post("/user/", data=register_data)

        Assertions.assert_status_code(response_register, 200)
        Assertions.assert_json_has_key(response_register, "id")

        email = register_data['email']
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

        # DELETE
        response_delete = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_status_code(response_delete, 200)

        # GET
        response_get = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_status_code(response_get, 404)
        assert response_get.text == "User not found", "Response text is not correct"

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test delete user authorized another user")
    def test_delete_user_auth_another(self):
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

        # DELETE USER 2
        response_edit = MyRequests.delete(
            f"/user/{user2_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_status_code(response_edit, 200)

        # GET
        response_get = MyRequests.get(
            f"/user/{user2_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_json_value_by_name(response_get, "username", "learnqa", "Cant find user_id")

