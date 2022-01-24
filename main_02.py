from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

Builder.load_file('layout.kv')

resource_add_path('font')
LabelBase.register(DEFAULT_FONT, 'NotoSansJP-Regular.otf')

Window.size = (600, 800)

class MyLayout(Widget):
    pass

class LoanSimulatorApp(App):
    def build(self):
        Window.clearcolor = (0.5,0.5,0.5,1)
        return MyLayout()


if __name__ == "__main__":
    LoanSimulatorApp().run()
