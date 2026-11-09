# Импортируем библиотеки
import datetime
import os
import requests


# Класс для логирования тестов
class Logger:
    # Файл для хранения логов
    file_name = f'logs/log_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'

    # Метод для записи данных в файл
    @classmethod
    def write_log_to_file(cls, data: str):
        # Открываем файл для записи данных
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    # Метод для логирования запроса
    @classmethod
    def add_request(cls, url: str, method: str):
        # Получаем название текущего теста
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        # Формируем данные для записи в лог
        data_to_add = f'\n-----\n'
        data_to_add += f'Test: {test_name}\n'
        data_to_add += f'Time: {str(datetime.datetime.now())}\n'
        data_to_add += f'Request method: {method}\n'
        data_to_add += f'Request URL: {url}\n'
        data_to_add += '\n'

        # Записываем данные в файл
        cls.write_log_to_file(data_to_add)

    # Метод для логирования ответа
    @classmethod
    def add_response(cls, result: requests.Response):
        # Получаем заголовки и cookies ответа
        headers_as_dict = dict(result.headers)
        cookies_as_dict = dict(result.cookies)

        # Формируем данные для записи в лог
        data_to_add = f'Response code: {result.status_code}\n'
        data_to_add += f'Response text: {result.text}\n'
        data_to_add += f'Response headers: {headers_as_dict}\n'
        data_to_add += f'Response cookies: {cookies_as_dict}\n'
        data_to_add += f'\n-----\n'

        # Записываем данные в файл
        cls.write_log_to_file(data_to_add)
