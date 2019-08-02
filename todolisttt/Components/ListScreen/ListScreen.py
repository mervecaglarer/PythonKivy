from threading import Timer
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.utils import get_color_from_hex

import json


class ListScreen(Screen):
    def __init__(self, **kwargs):
        super(ListScreen, self).__init__(**kwargs)
        self.name = 'ListScreen'

    def on_enter(self):
        file = open('C:\\Users\\Merve\\Desktop\\app\\pythonkivy\\data.json')
        file_read = file.read()
        file_data = json.loads(file_read)
        self.ids.left.clear_widgets()
        for object in file_data:
            newwBoxLayout = BoxLayout(orientation="horizontal", spacing=20, size_hint_y=None, height=60,id=object["task"])
            newwBoxLayout.bind(minimum_height=newwBoxLayout.setter("height"))

            Buttonn = Button(text="X", size_hint=(.1, None), height=30, on_press=self.remove_task)

            newLabel = ButtonLabel(size_hint=(1, None), height=30, id=object["task"],
                                   font_size="40sp",
                                   font_name="C:\\Users\\Merve\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Bangers-Regular.ttf",
                                   color=get_color_from_hex("#000000"),
                                   text=(str(object["task"]) +
                                     "                              " +
                                  (str(object["deadline"]))))
            newwBoxLayout.add_widget(newLabel)
            newwBoxLayout.add_widget(Buttonn)
            self.ids["left"].add_widget(newwBoxLayout)
            s=Timer(0.1,self.set_color)
            s.start()

    def set_color(self):
        children=self.ids["left"].children
        for child in children:
            with child.canvas.before:
                Color(rgba=get_color_from_hex("#fff"))
                Rectangle(pos=child.pos,size=child.size)

    def remove_task(self, instance):
        list = []
        file = open('C:\\Users\\Merve\\Desktop\\app\\pythonkivy\\data.json')
        file_read = file.read()
        file_data = json.loads(file_read)
        for x in file_data:
            list.append(x)
        for object in list:
            if instance.parent.id == object["task"]:
                list.remove(object)
                self.ids["left"].remove_widget(instance.parent)
        with open("data.json", "w") as jsonFile:
            json.dump(list, jsonFile)


class ButtonLabel(ButtonBehavior, Label):
    def __init__(self, **kwargs):
        super(ButtonLabel, self).__init__(**kwargs)

