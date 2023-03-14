import pytest
import requests
import json


class TestUserAgent:
    user_agents = [
        ('Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'),
        ('Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1'),
        ('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'),
        ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0'),
        ('Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1')
    ]

    @pytest.mark.parametrize('condition', user_agents, url)
    def test_user_agent(self, condition):
        expected_response_first_agent = "'platform': 'Mobile', 'browser': 'No', 'device': 'Android'"
        expected_response_second_agent = "'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'",
        expected_response_third_agent = "'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'",
        expected_response_fourth_agent = "'platform': 'Web', 'browser': 'Chrome', 'device': 'No'",
        expected_response_fifth_agent = "'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'"
        if condition == 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30':
            response_first_agent = requests.get('https://playground.learnqa.ru/ajax/api/user_agent_check', headers={'User-Agent': {condition}})
            obj_response_first_agent = json.dumps(response_first_agent)
            assert expected_response_first_agent == obj_response_first_agent["user_agent"][1]


