import pytest
import requests


class TestFirstAPI:
    names = [
        ("Roman"),
        ("Yana"),
        ("")
    ]

    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        name = "Roman"
        data = {"name": name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Status code is not 200"

        response_dict = response.json()
        assert "answer" in response_dict, "Cant find answer in response"

        expected_response_text = f'Hello, {name}'
        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_text, "Response text is not correct"
