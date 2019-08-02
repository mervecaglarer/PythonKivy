import time
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.lang.builder import Builder
from Components.HomeScreen.HomeScreen import HomeScreen
from Components.ListScreen.ListScreen import ListScreen
from Components.SM.SM import SM
Builder.load_file("C:\\Users\\Merve\\Desktop\\app\\pythonkivy\\Components\\HomeScreen\\HomeScreen.kv")
Builder.load_file("C:\\Users\\Merve\\Desktop\\app\\pythonkivy\\Components\\ListScreen\\ListScreen.kv")
Builder.load_file("C:\\Users\\Merve\\Desktop\\app\\pythonkivy\\Components\\SM\\SM.kv")

class MyApp(App):
    time = StringProperty()
    def update(self, *args):
        self.time = str(time.asctime())
    def build(self):
        self.title = "ToDoList"
        self.icon = 'C:\\Users\\Merve\\Desktop\\app\\pythonkivy\\todolist.png'
        Clock.schedule_interval(self.update, 1)
        return SM()


if __name__ == '__main__':
    MyApp().run()


