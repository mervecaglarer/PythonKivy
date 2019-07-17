from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class RootWidget(GridLayout):
    pass

class sosApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    sosApp().run()