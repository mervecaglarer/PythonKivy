from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
import json


class ListScreen(Screen):
    def __init__(self, **kwargs):
        super(ListScreen, self).__init__(**kwargs)
        self.name = 'ListScreen'
        self.ScrollBoxLayout = BoxLayout(orientation="vertical", id="box", size_hint=(1, .7), pos_hint={'top': .2})
        self.newScroolView = ScrollView(id="boxScroll", do_scroll_x=False, do_scroll_y=True, size=self.size,
                                        bar_width=5)

        self.newScroolView.add_widget(self.ScrollBoxLayout)
        self.add_widget(self.newScroolView)

    def on_enter(self):
        file = open('data')
        file_read = file.read()
        file_data = json.loads(file_read)

        for object in file_data:
            newLabel = ButtonLabel(
                text=(str(object["task"]) + " ---> " + str(object["deadline"])),
                size_hint=(1, None), height=50, id=object["deadline"], font_size='50')
            self.ScrollBoxLayout.add_widget(newLabel)


class ButtonLabel(ButtonBehavior, Label):
    def __init__(self, **kwargs):
        super(ButtonLabel, self).__init__(**kwargs)

    def on_press(self):
        file = open('data.json')
        file_read = file.read()
        file_data = json.loads(file_read)
