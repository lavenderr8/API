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
    def get_new_place(place_id) -> Response:
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
