from kivy.app import App
from kivy.uix.label import Label

from cerebellum.defaults import KIVY_TEMPLATES_PATH


class RootWidget(Label):
    pass


class CerebellumApp(App):
    kv_directory = KIVY_TEMPLATES_PATH

    def build(self):
        return RootWidget()
