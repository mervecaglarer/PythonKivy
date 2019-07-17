from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string("""
<RootWidget>:
    orientation: "vertical"
    BoxLayout:
        size_hint_y: 0.2
        Button:
            text: "one"
            size_hint_x: 0.2
        Button:
            text: "two"
            size_hint_x: 0.2
        Button:
            text: "three"
            size_hint_x: 0.2
        Button:
            text: "four"
            size_hint_x: 0.2

    GridLayout:
        cols: 2
        rows: 2
        Button:
            text: "1"
        Button:
            text: "3"
        Button:
            text: "2"
        Button:
            text: "4"
""")

class RootWidget(BoxLayout):
    pass

class boxApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    boxApp().run()