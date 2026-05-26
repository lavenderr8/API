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

        # Проверка обязательных полей POST
        Checking.check_json_token(
            result_post,
            expected_value=['status', 'place_id', 'scope', 'reference', 'id']
        )

        # Проверка значения поля status
        Checking.check_json_value(result_post, 'status', 'OK')

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

        # Проверка обязательных полей GET
        Checking.check_json_token(
            result_get,
            expected_value=[
                'location',
                'accuracy',
                'name',
                'phone_number',
                'address',
                'types',
                'website',
                'language'
            ]
        )

        # Проверка значения поля address
        Checking.check_json_value(
            result_get,
            'address',
            '29, side layout, cohen 09'
        )

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

        # Проверка обязательных полей PUT
        Checking.check_json_token(
            result_put,
            expected_value=['msg']
        )

        # Проверка значения поля msg
        Checking.check_json_value(
            result_put,
            'msg',
            'Address successfully updated'
        )

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

        # Проверка обязательных полей DELETE
        Checking.check_json_token(
            result_delete,
            expected_value=['status']
        )

        # Проверка значения поля status
        Checking.check_json_value(
            result_delete,
            'status',
            'OK'
        )
