import operator
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from models import Pizza


class PizzaWidget(BoxLayout):
    nom = StringProperty("")
    ingredients = StringProperty("")
    prix = NumericProperty(0.0)
    vegetarienne = BooleanProperty(False)


class MainWidget(BoxLayout):
    proprieteRecycleView = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pizzas=[
            Pizza("4 fromages", "chèvre, comté, emmental, brie", 9.5, True),
            Pizza("Chorizo", "tomates, chorizo, parmesan", 11.2, False),
            Pizza("Calzone", "fromage, jambon, champignons", 10, False),
        ]

    def construire_dictionnaire(self, pizza):
        return {
            "nom": pizza.nom,
            "ingredients": pizza.ingredients,
            "prix": pizza.prix,
            "vegetarienne": pizza.vegetarienne
        }

    def on_parent(self, widget, parent):
        liste_pizzas = [self.construire_dictionnaire(pizza) for pizza in self.pizzas]
        liste_pizzas.sort(key=operator.itemgetter("prix"))
        self.proprieteRecycleView.data = liste_pizzas


class PizzaApp(App):
    pass


PizzaApp().run()
