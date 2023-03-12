import requests


class TestUserAuth:
    def test_auth_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        assert "auth_sid" in response1.cookies, "Cant find auth cookie in response"
        assert "x-csrf-token" in response1.headers, "Cant find x-csrf-token in response"
        assert "user_id" in response1.json(), "Cant find user_id in response"

        authSid = response1.cookies.get("auth_sid")
        token = response1.headers.get("x-csrf-token")
        userIdFromAuth = response1.json()["user_id"]

        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token":token},
            cookies={"auth_sid": authSid}
        )

        assert "user_id" in response2.json(),"Cant find user_id in response2"

        userIdFromCheck = response2.json()["user_id"]
        assert userIdFromAuth == userIdFromCheck, "user_id from Auth is not equal to user_id from Check"