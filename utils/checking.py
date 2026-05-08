from requests import Response


# Класс для проверок
class Checking:

    # Метод для проверки статус-кода
    @staticmethod
    def check_status_code(response: Response, status_code):
        # Проверка статус-кода
        assert status_code == response.status_code

        # Вывод успешного статус-кода
        print("Успешно! Статус-код: " + str(response.status_code))
