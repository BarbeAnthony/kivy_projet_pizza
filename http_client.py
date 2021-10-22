import json

from kivy.network.urlrequest import UrlRequest


class HttpClient:

    def get_pizzas(self, on_complete):

        url = "https://abarbepizzamamadjango.herokuapp.com/api/GetPizzas"

        def data_received(req, result):
            data = json.loads(result)
            pizzas_dict = [pizza["fields"] for pizza in data]
            if on_complete:
                on_complete(pizzas_dict)

        UrlRequest(url, on_success=data_received)
