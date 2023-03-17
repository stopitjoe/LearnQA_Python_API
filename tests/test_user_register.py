import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime

class TestUserRegister(BaseCase):
    def setup_method(self):
        base_part = 'learnqa'
        domain = 'example.com'
        random_part = datetime.now().strftime('%m%d%Y%H%M%S')
        self.email = f'{base_part}{random_part}@{domain}'

    def test_create_user_success(self):
        url_request = 'https://playground.learnqa.ru/api/user'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learqa',
            'lastName': 'learnqa',
            'email': self.email
        }

        response = requests.post(url_request, data=data)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, 'id')

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        url_request = 'https://playground.learnqa.ru/api/user'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learqa',
            'lastName': 'learnqa',
            'email': email
        }

        response = requests.post(url_request, data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode('UTF-8') == f"Users with email '{email}' already exists", f"Content is not correct - {response.content}" # Декодируем байтовый ответ в UTF-8 и сравниваем с ожидаемым результатом
