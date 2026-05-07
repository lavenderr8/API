"""
Файл для хранения HTTP-методов.
Используется в автотестах для отправки запросов.
"""

# Импортируем библиотеку
import requests


# Класс для работы с HTTP-запросами
class HTTPMethods:
    # Заголовки по умолчанию
    headers = {'Content-type': 'application/json'}

    # Cookie по умолчанию
    cookie = ""

    # Статические методы для HTTP-запросов:
    # GET, POST, PUT, DELETE.
    # Каждый метод отправляет запрос и возвращает ответ сервера

    @staticmethod
    def get(url):
        result = requests.get(
            url,
            headers=HTTPMethods.headers,
            cookie=HTTPMethods.cookie
        )
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(
            url,
            json=body,
            headers=HTTPMethods.headers,
            cookie=HTTPMethods.cookie
        )
        return result

    @staticmethod
    def put(url, body):
        result = requests.put(
            url,
            json=body,
            headers=HTTPMethods.headers,
            cookie=HTTPMethods.cookie
        )
        return result

    @staticmethod
    def delete(url, body):
        result = requests.delete(
            url,
            json=body,
            headers=HTTPMethods.headers,
            cookie=HTTPMethods.cookie
        )
        return result
