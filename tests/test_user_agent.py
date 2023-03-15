import pytest
import requests

request_url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
expected_response_first_agent = {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'}
expected_response_second_agent = {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'}
expected_response_third_agent = {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'}
expected_response_fourth_agent = {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'}
expected_response_fifth_agent = {'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'}
user_agents = [
    ('Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'),
    ('Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1'),
    ('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0'),
    ('Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1')
]


class TestUserAgent:
    @pytest.mark.parametrize('condition', user_agents)
    def test_user_agent(self, condition):
        if condition == 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30': # 1 request
            response_first_agent = requests.get(request_url, headers={'User-Agent': str({condition})}).json()
            del response_first_agent['user_agent']
            assert expected_response_first_agent == response_first_agent, f'First response: "{response_first_agent}" is not equal for first expected result: "{expected_response_first_agent}"'
        elif condition == 'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1': # 2 request
            response_second_agent = requests.get(request_url, headers={'User-Agent': str({condition})}).json()
            del response_second_agent['user_agent']
            assert expected_response_second_agent == response_second_agent, f'Second response: "{response_second_agent}" is not equal for second expected result: "{expected_response_second_agent}"'
        elif condition == 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)': # 3 request
            response_third_agent = requests.get(request_url, headers={'User-Agent': str({condition})}).json()
            del response_third_agent['user_agent']
            assert expected_response_third_agent == response_third_agent, f'Third response: "{response_third_agent}" is not equal for third expected result: "{expected_response_third_agent}"'
        elif condition == 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0': # 4 request
            response_fourth_agent = requests.get(request_url, headers={'User-Agent': str({condition})}).json()
            del response_fourth_agent['user_agent']
            assert expected_response_fourth_agent == response_fourth_agent, f'Fourth response: "{response_fourth_agent}" is not equal for fourth expected result: "{expected_response_fourth_agent}"'
        elif condition == 'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1': # 5 requset
            response_fifth_agent = requests.get(request_url, headers={'User-Agent': str({condition})}).json()
            del response_fifth_agent['user_agent']
            assert expected_response_fifth_agent == response_fifth_agent, f'Fifth response: "{response_fifth_agent}" is not equal for fifth expected result: "{expected_response_fifth_agent}"'
