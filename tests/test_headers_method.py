import requests


class TestHeadersMethod:
    def test_method_headers(self):
        expected_header = "Some secret value"
        headers = requests.get('https://playground.learnqa.ru/api/homework_header').headers['x-secret-homework-header']
        print(f'Headers is "{headers}"')
        assert str(headers) == str(expected_header), f'Header is not correct: {expected_header} != {headers}'
