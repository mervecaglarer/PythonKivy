from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

import json

file = open("data")
file_read = file.read()
file_data = json.loads(file_read)
arr = []
for x in file_data:
    arr.append(x)


class MenuScreen(BoxLayout, Screen):
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
        task = self.ids.adding.text
        deadline = self.ids.deadline.text
        new = {"task": task, "deadline": deadline}
        arr.append(new)
        with open("data", "w") as outfile:
            json.dump(arr, outfile)
