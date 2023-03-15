import requests


class TestCookieMethod:
    def test_method_cookie(self):
        cookie = requests.get('https://playground.learnqa.ru/api/homework_cookie').cookies
        expected_cookie = "<RequestsCookieJar[<Cookie HomeWork=hw_value for .playground.learnqa.ru/>]>"
        print(f'cookie is "{cookie}"')
        assert str(cookie) == expected_cookie, f'Cookie is not correct: {cookie} != {expected_cookie}'
