from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
import datetime
import json


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Clock.schedule_interval(self.ClockFunc, 5)

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
        new = {"task": task, "deadline": deadline, "control": False}
        self.arr.append(new)
        with open("data", "w") as outfile:
            json.dump(self.arr, outfile)

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

        self.file = open('data')
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

                    the_popup = Popup(title="TIME IS UP", content=bx, size_hint=(None, None),
                                      size=(350, 150))
                    lb=Label(text="Today there are  " + str(count)+ "  tasks left to do!",size_hint=(.9,.2),pos_hint={"x":0,"y":.5})
                    btn = Button(text="OK",size_hint=(.2,.1),pos_hint={"x":.1,"y":0},on_press=the_popup.dismiss)
                    bx.add_widget(lb)
                    bx.add_widget(btn)


                    the_popup.open()
                    with open("data", "w") as jsonFile:
                        json.dump(self.file_data, jsonFile)
                    break
