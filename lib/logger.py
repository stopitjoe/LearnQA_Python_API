import datetime
import os
from requests import Response


class Logger:
    file_name = f"logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    @classmethod
    def _write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls, url: str, data: dict, headers: dict, cookies: dict, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add_request = f"\n-----\n"
        data_to_add_request += f"Test: {test_name}\n"
        data_to_add_request += f"Time: {str(datetime.datetime.now())}\n"
        data_to_add_request += f"Request method: {method}\n"
        data_to_add_request += f"Request URL: {url}\n"
        data_to_add_request += f"Request data: {data}\n"
        data_to_add_request += f"Request header: {headers}\n"
        data_to_add_request += f"Request cookie: {cookies}\n"
        data_to_add_request += "\n"

        cls._write_log_to_file(data_to_add_request)

    @classmethod
    def add_response(cls, response: Response):
        cookies_as_dict = dict(response.cookies)
        headers_as_dict = dict(response.headers)

        data_to_add_response = f"Response code: {response.status_code}\n"
        data_to_add_response += f"Response text: {response.text}\n"
        data_to_add_response += f"Response header: {headers_as_dict}\n"
        data_to_add_response += f"Response cookies: {cookies_as_dict}\n"
        data_to_add_response += f"\n-----\n"

        cls._write_log_to_file(data_to_add_response)
