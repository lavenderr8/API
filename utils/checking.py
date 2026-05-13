import json

from requests import Response


# Класс для проверок
class Checking:

    # Метод для проверки статус-кода
    @staticmethod
    def check_status_code(response: Response, status_code: int):

        # Проверка статус-кода
        assert status_code == response.status_code, \
            "Неверный статус-код! Ожидался: " + str(status_code) + \
            ", получен: " + str(response.status_code)

        # Вывод успешного статус-кода
        print("Успешно! Статус-код: " + str(response.status_code))

    # Метод для проверки обязательных полей
    @staticmethod
    def check_json_token(response: Response, expected_value: list):

        # Получение JSON ответа
        token = json.loads(response.text)

        # Проверка наличия обязательных полей
        assert list(token) == expected_value, \
            "Поля в ответе не совпадают"

        # Вывод успешной проверки полей
        print("Все поля присутствуют")