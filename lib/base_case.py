import json.decoder
from requests import Response
from datetime import datetime

class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f'Cant find cookie "{cookie_name}" in response'
        return response.cookies[cookie_name]

    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, f'Cant find headers "{headers_name}" in response'
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text - '{response.text}'"
        assert name in response_as_dict, f"Cant find in JSON a key '{name}'"
        return response_as_dict[name]

    def prepare_registration_data(self, email=None, user_name=None):
        if not email:
            base_part = 'learnqa'
            domain = 'example.com'
            random_part = datetime.now().strftime('%m%d%Y%H%M%S')
            email = f"{base_part}{random_part}@{domain}"
        if not user_name:
            user_name = 'learnqa'
        return {
            'password': '123',
            'username': user_name,
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }


