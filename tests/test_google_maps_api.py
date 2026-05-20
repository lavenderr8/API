from utils.api import GoogleMapsApi
from utils.checking import Checking


class TestCreatePlace:

    # Тест POST метода
    def test_create_new_place(self):
        # Метод POST
        print("\nМетод POST")

        # Вызов POST метода
        result_post = GoogleMapsApi.create_new_place()

        # Проверка POST
        Checking.check_status_code(result_post, 200)

        # Проверка значения поля status
        check_post = result_post.json()

        assert check_post["status"] == "OK", \
            "Неверное значение поля status"

        print("POST message корректный")

    # Тест GET метода
    def test_get_new_place(self):
        # Метод POST
        print("\nМетод POST")

        # Вызов POST метода
        result_post = GoogleMapsApi.create_new_place()

        # Получаем place_id из ответа POST
        place_id = result_post.json()["place_id"]

        # Метод GET
        print("\nМетод GET")

        # Вызов GET метода
        result_get = GoogleMapsApi.get_new_place(place_id)

        # Проверка GET
        Checking.check_status_code(result_get, 200)

    # Тест PUT метода
    def test_put_new_place(self):
        # Метод POST
        print("\nМетод POST")

        # Вызов POST метода
        result_post = GoogleMapsApi.create_new_place()

        # Получаем place_id из ответа POST
        place_id = result_post.json()["place_id"]

        # Метод PUT
        print("\nМетод PUT")

        # Вызов PUT метода
        result_put = GoogleMapsApi.put_new_place(place_id)

        # Проверка PUT
        Checking.check_status_code(result_put, 200)

        # Проверка сообщения PUT
        check_put = result_put.json()

        assert check_put["msg"] == "Address successfully updated", \
            "Неверное значение поля msg"

        print("PUT message корректный")

    # Тест DELETE метода
    def test_delete_new_place(self):
        # Метод POST
        print("\nМетод POST")

        # Вызов POST метода
        result_post = GoogleMapsApi.create_new_place()

        # Получаем place_id из ответа POST
        place_id = result_post.json()["place_id"]

        # Метод DELETE
        print("\nМетод DELETE")

        # Вызов DELETE метода
        result_delete = GoogleMapsApi.delete_new_place(place_id)

        # Проверка DELETE
        Checking.check_status_code(result_delete, 200)

        # Проверка значения поля status
        check_delete = result_delete.json()

        assert check_delete["status"] == "OK", \
            "Неверное значение поля status"

        print("DELETE message корректный")
