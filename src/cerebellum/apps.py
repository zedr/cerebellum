from kivy.app import App

from kivy.uix.widget import Widget
from cerebellum.defaults import KIVY_TEMPLATES_PATH


class RootWidget(Widget):
    pass


class TemplateApp(App):
    kv_directory = KIVY_TEMPLATES_PATH

    def build(self):
        return Widget()
