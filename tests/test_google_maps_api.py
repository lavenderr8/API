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

        # Метод PUT
        print("\nМетод PUT")

        # Вызов PUT метода
        result_put: Response = GoogleMapsApi.put_new_place(place_id)

        # Проверка PUT
        assert result_put.status_code == 200
        print("PUT запрос отработал, статус код 200")

        # Проверка сообщения PUT
        check_put = result_put.json()
        assert check_put["msg"] == "Address successfully updated"
        print("PUT message корректный")

        # Метод DELETE
        print("\nМетод DELETE")

        # Вызов DELETE метода
        result_delete: Response = GoogleMapsApi.delete_new_place(place_id)

        # Проверка DELETE
        assert result_delete.status_code == 200
        print("DELETE запрос отработал, статус код 200")

        # Проверка значения поля status
        check_delete = result_delete.json()
        assert check_delete["status"] == "OK"
        print("DELETE message корректный")
