"""
Файл для хранения HTTP-методов.
Используется в автотестах для отправки запросов.
"""

# Импортируем библиотеку
import requests

from utils.logger import Logger


# Класс для работы с HTTP-запросами
class HTTPMethods:
    # Заголовки по умолчанию
    headers = {'Content-type': 'application/json'}

    # Cookie по умолчанию
    cookie = {}

    # GET запрос
    @staticmethod
    def get(url: str) -> requests.Response:
        # Логируем запрос
        Logger.add_request(url, method='GET')

        # Отправляем GET запрос
        result = requests.get(
            url,
            headers=HTTPMethods.headers,
            cookies=HTTPMethods.cookie,
            timeout=10
        )

        # Логируем ответ
        Logger.add_response(result)
        return result

    # POST запрос
    @staticmethod
    def post(url: str, body: dict) -> requests.Response:
        # Логируем запрос
        Logger.add_request(url, method='POST')

        # Отправляем POST запрос
        result = requests.post(
            url,
            json=body,
            headers=HTTPMethods.headers,
            cookies=HTTPMethods.cookie,
            timeout=10
        )

        # Логируем ответ
        Logger.add_response(result)
        return result

    # PUT запрос
    @staticmethod
    def put(url: str, body: dict) -> requests.Response:
        # Логируем запрос
        Logger.add_request(url, method='PUT')

        # Отправляем PUT запрос
        result = requests.put(
            url,
            json=body,
            headers=HTTPMethods.headers,
            cookies=HTTPMethods.cookie,
            timeout=10
        )

        # Логируем ответ
        Logger.add_response(result)
        return result

    # DELETE запрос
    @staticmethod
    def delete(url: str, body: dict | None = None) -> requests.Response:
        # Логируем запрос
        Logger.add_request(url, method='DELETE')

        # Отправляем DELETE запрос
        result = requests.delete(
            url,
            json=body,
            headers=HTTPMethods.headers,
            cookies=HTTPMethods.cookie,
            timeout=10
        )

        # Логируем ответ
        Logger.add_response(result)
        return result
