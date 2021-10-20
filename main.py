from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from models import Pizza


class MainWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pizzas=[
            Pizza("4 fromages", "chèvre, comté, emmental, brie", 9.5, True),
            Pizza("Chorizo", "tomates, chorizo, parmesan", 11.2, False),
            Pizza("Calzone", "fromage, jambon, champignons", 10, False),
        ]


class PizzaApp(App):
    pass

PizzaApp().run()
