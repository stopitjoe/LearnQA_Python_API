import json.decoder

from requests import Response

class BaseCase:
    def get_cooke(self, response: Response, cookie_name):
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