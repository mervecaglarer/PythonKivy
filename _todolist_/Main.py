import time

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from pythonkivy.Components.SM.SM import SM
from kivy.lang.builder import Builder
from pythonkivy.Components.HomeScreen.HomeScreen import HomeScreen
from pythonkivy.Components.ListScreen.ListScreen import ListScreen
Builder.load_file("Components/HomeScreen/HomeScreen.kv")
Builder.load_file("Components/ListScreen/ListScreen.kv")
Builder.load_file("Components/SM/SM.kv")

class MyApp(App):
    time = StringProperty()
    def update(self, *args):
        self.time = str(time.asctime())
    def build(self):
        self.title = "ToDoList"
        self.icon = 'C:\\Users\\Merve\\PycharmProjects\\PythonKivy\\pythonkivy\\list.png'
        Clock.schedule_interval(self.update, 1)
        return SM()


if __name__ == '__main__':
    MyApp().run()


