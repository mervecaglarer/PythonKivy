from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string("""
<RootWidget>:
    orientation: "horizontal"
    Button:
        text: "1.button"
        font_size: "50sp"
    Button:
        text: "2.button"
    Button:
        text: "3.button"
    Button:
        text: "4.button"
""")
class RootWidget(BoxLayout):
    pass

class buttonApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    buttonApp().run()