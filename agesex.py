from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_string("""

<MyApp>
    GridLayout:
        cols: 1
        size: root.width - 200 , root.height - 200
        pos: 100 , 100

        GridLayout:
            cols: 2

            Label:
                text: "Age:"
            TextInput:
                multiline: False
            Label:
                text: "Sex:"
            TextInput:
                multiline: False
        Button:
            text: "Submit"
""")

class MyApp(Widget):
    pass

class TestApp(App):
    def build(self):
        return MyApp()
if __name__ == "__main__":
    TestApp().run()