from requests import Response
import json

class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message): ### Проверка значения ключа JSON по его имени
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not JSON format, Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesnt have key'{name}'"
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name): ### Проверка наличия ключа в JSON по его имени
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not JSON format, Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesnt have key'{name}'"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list): ### Проверка наличия множества ключей в JSON по их имени
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not JSON format, Response text is '{response.text}'"
        for name in names:
            assert name in response_as_dict, f"Response JSON doesnt have key'{name}'"

    @staticmethod
    def assert_json_has_not_key(response: Response, name): ### Проверка отсутствия ключа в JSON по его имени
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not JSON format, Response text is '{response.text}'"

        assert name not in response_as_dict, f"Response JSON have key'{name}'. Expected its not"

    @staticmethod
    def assert_json_has_not_keys(response: Response, names: list): ### Проверка отсутствия множества ключей в JSON по их имени
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not JSON format, Response text is '{response.text}'"
        for name in names:
            assert name not in response_as_dict, f"Response JSON have key'{name}'. Expected its not"

    @staticmethod
    def assert_status_code(response: Response, expected_status_code): ### Проверка соответствия статус кода
        assert response.status_code == expected_status_code, \
            f'Unexpected status-code: {response.status_code}. Expected: {expected_status_code}'
