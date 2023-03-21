import allure
import pytest

from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


@allure.epic("Register cases")
class TestUserRegister(BaseCase):
    exclude_params = [
        ('password'),
        ('username'),
        ('firstName'),
        ('lastName'),
        ('email')
    ]

    @allure.description("Create user success")
    def test_create_user_success(self): #------------------------------------------- Успешное создание пользователя.
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, 'id')

    @allure.description("Create user with existing email")
    def test_create_user_with_existing_email(self): #-------------------------------- Не успешное создание пользователя с существующим email
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode('utf-8') == f"Users with email '{email}' already exists", \
            f"Content is not correct - {response.content}"

    @allure.description("Create user with incorrect email - missing '@'")
    def test_create_user_incorrect_email(self):#----------------------------------- Не успешное создание пользователя с некорректным email
        email = 'vinkotovexample.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode('utf-8') == f"Invalid email format", \
            f"Content is not correct - {response.content}"

    @allure.description("Create user without some parameter")
    @pytest.mark.parametrize('condition', exclude_params)
    def test_create_user_without_param(self, condition): #-------------------------- Не успешное создание пользователя с отсутствием одного параметра
        if condition == 'password':
            data = self.prepare_registration_data()
            del data[condition]

            response = MyRequests.post("/user/", data=data)

            Assertions.assert_status_code(response, 400)
            assert response.content.decode('utf-8') == f"The following required params are missed: {condition}"

        elif condition == 'username':
            data = self.prepare_registration_data()
            del data[condition]

            response = MyRequests.post("/user/", data=data)

            Assertions.assert_status_code(response, 400)
            assert response.content.decode('utf-8') == f"The following required params are missed: {condition}"

        elif condition == 'firstName':
            data = self.prepare_registration_data()
            del data[condition]

            response = MyRequests.post("/user/", data=data)

            Assertions.assert_status_code(response, 400)
            assert response.content.decode('utf-8') == f"The following required params are missed: {condition}"

        elif condition == 'lastName':
            data = self.prepare_registration_data()
            del data[condition]

            response = MyRequests.post("/user/", data=data)

            Assertions.assert_status_code(response, 400)
            assert response.content.decode('utf-8') == f"The following required params are missed: {condition}"

        elif condition == 'email':
            data = self.prepare_registration_data()
            del data[condition]

            response = MyRequests.post("/user/", data=data)

            Assertions.assert_status_code(response, 400)
            assert response.content.decode('utf-8') == f"The following required params are missed: {condition}"

        else:
            print(f"Incorrect data:{self.prepare_registration_data()}")
