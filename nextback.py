from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<firstscreen>:
    Button:
        text: "next"
        on_release: root.manager.current = root.manager.next()
<controlscreen>:
    Button:
        text: "back"
        on_release: root.manager.current = root.manager.previous()
""")
class firstscreen(Screen):
    pass

class controlscreen(Screen):
    pass

class screenApp(App):
    def build(self):
        root = ScreenManager()
        root.add_widget(firstscreen(name = "first screen"))
        root.add_widget(controlscreen(name = "control screen"))
        return root

if __name__ == "__main__":
    screenApp().run()

