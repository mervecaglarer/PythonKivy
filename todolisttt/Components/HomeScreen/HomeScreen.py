from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
import datetime
import json


class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.ClockFunc, 3600)

    def add(self):
        file = open("C:\\Users\\Merve\\Desktop\\app\\pythonkivy\\data.json")
        file_read = file.read()
        file_data = json.loads(file_read)
        arr = []
        for i in file_data:
            arr.append(i)
        file.close()
        task = self.ids.task.text
        deadline = self.ids.deadline.text
        new = {"task": task, "deadline": deadline, "control": False}
        arr.append(new)
        with open("data.json", "w") as outfile:
            json.dump(arr, outfile)
    def empty(self):
        self.ids.task.text=""
        self.ids.deadline.text=""
    def ClockFunc(self, *args):
        date = datetime.datetime.now()
        day = date.day
        month = date.month
        if day < 10:
            gun = "0" + str(day)
        else:
            gun = str(day)
        if month < 10:
            ay = "0" + str(month)
        else:
            ay = str(month)
        instant = gun + "/" + ay

        self.file = open('data.json')
        self.file_read = self.file.read()
        self.file_data = json.loads(self.file_read)
        count = 0
        for object in self.file_data:
            if object["deadline"] == instant:
                if object["control"] == False:
                    count = count + 1
        for object in self.file_data:
            if object["deadline"] == instant:
                if object["control"] == False:
                    bx = BoxLayout()
                    the_popup = Popup(title="TODAY", content=bx, size_hint=(None, None), size=(350, 150))
                    lb = Label(text="There are  " + str(count) + "  tasks left to do!", size_hint=(.9, .2),
                               pos_hint={"x": 0, "y": .5})
                    bx.add_widget(lb)
                    the_popup.open()

                    with open("data.json", "w") as jsonFile:
                        json.dump(self.file_data, jsonFile)
                    break
