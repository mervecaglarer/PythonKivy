from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

Builder.load_file("Components/ListScreen/ListScreen.kv")
import json


class ListScreen(Screen):
    def __init__(self, **kwargs):
        super(ListScreen, self).__init__(**kwargs)
        self.name = 'ListScreen'

    def on_enter(self):
        file = open('data')
        file_read = file.read()
        file_data = json.loads(file_read)
        self.ids.left.clear_widgets()

        for object in file_data:
            newwBoxLayout = BoxLayout(orientation="horizontal", spacing=20, size_hint_y=None, height=30,
                                      id=object["task"])
            newwBoxLayout.bind(minimum_height=newwBoxLayout.setter("height"))

            Buttonn = Button(text="X", size_hint=(.1, None), height=30, on_press=self.remove_task)
            newLabel = ButtonLabel(size_hint=(1, None), height=30, id=object["task"], strikethrough=object["control"],
                                   text=(str(object["task"]) + "           " + (str(object["deadline"]))))
            newwBoxLayout.add_widget(newLabel)
            newwBoxLayout.add_widget(Buttonn)
            self.ids["left"].add_widget(newwBoxLayout)

    def remove_task(self, instance):
        list = []
        file = open('data')
        file_read = file.read()
        file_data = json.loads(file_read)
        for x in file_data:
            list.append(x)
        for y in list:
            for object in list:
                if instance.parent.id == object["task"]:
                    list.remove(object)
                    self.ids["left"].remove_widget(instance.parent)
        with open("data", "w") as jsonFile:
            json.dump(list, jsonFile)


class ButtonLabel(ButtonBehavior, Label):
    def __init__(self, **kwargs):
        super(ButtonLabel, self).__init__(**kwargs)

    def on_press(self):
        file = open('data')
        file_read = file.read()
        file_data = json.loads(file_read)

        for object in file_data:
            if self.id == object["task"]:
                if self.strikethrough == True:
                    self.strikethrough = False
                    object["control"] = False
                elif self.strikethrough == False:
                    self.strikethrough = True
                    object["control"] = True

        with open("data", "w") as jsonFile:
            json.dump(file_data, jsonFile)
