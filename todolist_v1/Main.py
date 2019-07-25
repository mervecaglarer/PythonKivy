from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from todolist.Components.SM.SM import SM
from datetime import time
from todolist.Components.ListScreen.ListScreen import ListScreen
from todolist.Components.CalendarScreen import CalendarScreen

Builder.load_file("Components/CalendarScreen/select.kv")
Builder.load_file("Components/CalendarScreen/status.kv")
Builder.load_file("Components/CalendarScreen/CalendarScreen.kv")

Builder.load_file("Components/SM/SM.kv")
Builder.load_file("Components/MenuScreen/MenuScreen.kv")
Builder.load_file("Components/ListScreen/ListScreen.kv")
import json

file = open("data")
file_read = file.read()
file_data = json.loads(file_read)
arr = []
for x in file_data:
    arr.append(x)


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    file = open("data")
    file_read = file.read()
    file_data = json.loads(file_read)
    arr = []
    file.close()
    for i in file_data:
        arr.append(i)

    def add(self):
        task = self.ids.task.text
        deadline = self.ids.deadline.text
        new = {"task": task, "deadline": deadline}
        arr.append(new)
        with open("data", "w") as outfile:
            json.dump(arr, outfile)


class ListScreen(Screen):
    pass


class MyApp(App):
    def build(self):
        self.title = "ToDoList"
        return SM()


if __name__ == '__main__':
    MyApp().run()
