import requests


class TestHeadersMethod:
    def test_method_headers(self):
        headers = requests.get('https://playground.learnqa.ru/api/homework_header').headers
        print(f'Headers is "{headers}"')
        assert headers != "", f'Cant find headers in response'
