from kivy.app import App
from kivy.uix.screenmanager import Screen
from pythonkivy.Components.SM.SM import SM
from kivy.lang.builder import Builder
from pythonkivy.Components.HomeScreen.HomeScreen import HomeScreen
from pythonkivy.Components.ListScreen.ListScreen import ListScreen
Builder.load_file("Components/HomeScreen/HomeScreen.kv")
Builder.load_file("Components/ListScreen/ListScreen.kv")
Builder.load_file("Components/SM/SM.kv")

class MyApp(App):
    def build(self):
        self.title = "ToDoList"
        return SM()


if __name__ == '__main__':
    MyApp().run()


