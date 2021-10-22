import operator
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import CoverBehavior

from http_client import HttpClient
from models import Pizza


class MainWidget(FloatLayout):
    proprieteRecycleView = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        HttpClient().get_pizzas(self.on_server_data)

    def on_server_data(self, pizzas_dict):
        pizzas_dict.sort(key=operator.itemgetter("prix"))
        self.proprieteRecycleView.data = pizzas_dict


class PizzaWidget(BoxLayout):
    nom = StringProperty("")
    ingredients = StringProperty("")
    prix = NumericProperty(0.0)
    vegetarienne = BooleanProperty(False)


class PizzaApp(App):
    pass


PizzaApp().run()
