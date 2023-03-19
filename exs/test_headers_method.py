import requests


class TestHeadersMethod:
    def test_method_headers(self):
        expected_header = "Some secret value"
        headers = requests.get('https://playground.learnqa.ru/api/homework_header').headers['x-secret-homework-header']
        print(f'Headers is "{headers}"')
        assert str(headers) == str(expected_header), f'Header is not correct: {expected_header} != {headers}'

# class TestHeadersMethod:
#     def test_method_headers(self):
#         api_url = 'https://playground.learnqa.ru/api/homework_header'
#         expected_header_value = "Some secret value"
#
#         try:
#             response = requests.get(api_url)
#
#             print(f'Response status code: {response.status_code}')
#             print(f'Response text: {response.text}')
#
#             if 'x-secret-homework-header' in response.headers:
#                 header_value = response.headers['x-secret-homework-header']
#
#                 assert header_value == expected_header_value, f'Header value "{header_value}" does not match expected value "{expected_header_value}"'
#             else:
#                 raise AssertionError('Header x-secret-homework-header not found in response headers')
#
#         except requests.exceptions.RequestException as e:
#             raise AssertionError(f'Error making request to API: {e}')