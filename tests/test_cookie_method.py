import requests


class TestCookieMethod:
    def test_method_cookie(self):
        cookie = requests.get('https://playground.learnqa.ru/api/homework_cookie').cookies
        print(f'cookie is "{cookie}"')
        assert cookie != "", f'Cant find cookie in response'
