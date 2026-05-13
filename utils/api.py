from requests import Response
from utils.http_methods import HTTPMethods


class GoogleMapsApi:
    # Базовый URL
    base_url = "https://rahulshettyacademy.com"

    # Параметр для всех запросов
    key = "?key=qaclick123"

    # POST запрос - создание нового места
    @staticmethod
    def create_new_place() -> Response:
        # Тело POST запроса
        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        # Ресурс метода POST
        post_resource = "/maps/api/place/add/json"

        # Полный URL
        post_url = GoogleMapsApi.base_url + post_resource + GoogleMapsApi.key
        print(post_url)

        # Выполнение POST запроса
        result_post = HTTPMethods.post(post_url, json_for_create_new_place)

        # Вывод ответа
        print(result_post.text)

        return result_post

    # GET запрос - получение места
    @staticmethod
    def get_new_place(place_id: str) -> Response:
        # Ресурс метода GET
        get_resource = "/maps/api/place/get/json"

        # Полный URL
        get_url = GoogleMapsApi.base_url + get_resource + GoogleMapsApi.key + "&place_id=" + place_id
        print(get_url)

        # Выполнение GET запроса
        result_get = HTTPMethods.get(get_url)

        # Вывод ответа
        print(result_get.text)

        return result_get

    # PUT запрос - изменение места
    @staticmethod
    def put_new_place(place_id: str) -> Response:
        # Ресурс метода PUT
        put_resource = "/maps/api/place/update/json"

        # Полный URL
        put_url = GoogleMapsApi.base_url + put_resource + GoogleMapsApi.key
        print(put_url)

        # Тело PUT запроса
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }

        # Выполнение PUT запроса
        result_put = HTTPMethods.put(put_url, json_for_update_new_location)

        # Вывод ответа
        print(result_put.text)

        return result_put

    # DELETE запрос - удаление места
    @staticmethod
    def delete_new_place(place_id: str) -> Response:
        # Ресурс метода DELETE
        delete_resource = "/maps/api/place/delete/json"

        # Полный URL
        delete_url = GoogleMapsApi.base_url + delete_resource + GoogleMapsApi.key
        print(delete_url)

        # Тело DELETE запроса
        json_for_delete_new_location = {
            "place_id": place_id
        }

        # Выполнение DELETE запроса
        result_delete = HTTPMethods.delete(delete_url, json_for_delete_new_location)

        # Вывод ответа
        print(result_delete.text)

        return result_delete
