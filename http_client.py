import json

from kivy.network.urlrequest import UrlRequest


class HttpClient:

    def get_pizzas(self, on_complete, on_error):

        url = "https://abarbepizzamamadjango.herokuapp.com/api/GetPizzas"

        def data_received(req, result):
            data = json.loads(result)
            pizzas_dict = [pizza["fields"] for pizza in data]
            if on_complete:
                on_complete(pizzas_dict)

        def data_error(req, error):
            if on_error:
                on_error(str(error))

        def data_failure(req, result):
            if on_error:
                on_error("Erreur du serveur : " + str(req.resp_status))

        UrlRequest(url, on_success=data_received, on_error=data_error, on_failure=data_failure)
