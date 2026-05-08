from requests import Response
from utils.api import GoogleMapsApi


class TestCreatePlace:

    def test_create_new_place(self):
        # Вызов POST метода
        result_post: Response = GoogleMapsApi.create_new_place()

        # Проверка статус-кода
        assert result_post.status_code == 200
        print("Статус код 200")

        # Проверка значения поля status
        check_status = result_post.json()
        assert check_status["status"] == "OK"
        print("Поле status = OK")
