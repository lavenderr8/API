from requests import Response
from utils.api import GoogleMapsApi


class TestCreatePlace:

    def test_create_new_place(self):
        # Метод POST
        print("\nМетод POST")

        # Вызов POST метода
        result_post: Response = GoogleMapsApi.create_new_place()

        # Получаем place_id из ответа POST
        place_id = result_post.json()["place_id"]

        # Проверка POST
        assert result_post.status_code == 200
        print("POST запрос отработал, статус код 200")

        # Метод GET
        print("\nМетод GET")

        # Вызов GET метода
        result_get: Response = GoogleMapsApi.get_new_place(place_id)

        # Проверка GET
        assert result_get.status_code == 200
        print("GET запрос отработал, статус код 200")

        # Проверка значения поля status
        check_status = result_post.json()
        assert check_status["status"] == "OK"
        print("Поле status = OK")
