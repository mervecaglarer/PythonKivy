import calendar
import time
import datetime
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.uix.screenmanager import Screen

Builder.load_file('Components/CalendarScreen/select.kv')
Builder.load_file('Components/CalendarScreen/status.kv')


# class for CalendarScreen.kv
class CalendarScreen(Screen):
    def __init__(self, **kwargs):
        super(CalendarScreen, self).__init__(**kwargs)


# -------------------------------------------------#


# class for status.kv
class Status(BoxLayout, EventDispatcher):

    def __init__(self, **kwargs):
        super(Status, self).__init__(**kwargs)


# -------------------------------------------------#


# class for select.kv
class Select(BoxLayout):
    n = ListProperty()
    day = ObjectProperty(None)
    month = ObjectProperty(None)
    lbl_ = ObjectProperty(None)
    btn = ObjectProperty(None)
    lb2_ = ObjectProperty(None)
    btn2 = ObjectProperty(None)
    hour = ObjectProperty(None)
    minute = ObjectProperty(None)
    global count

    def __init__(self, **kwargs):
        super(Select, self).__init__(**kwargs)
        self.count = 0

    def get_day(self):
        if self.count == 0:
            for i in range(1, 32):
                if i < 10:
                    self.n.append('0' + str(i))
                else:
                    self.n.append(str(i))
        self.count = 1
        self.day.values = self.n

    def get_month(self):
        if self.count == 0:
            for i in range(1, 13):
                if i < 10:
                    self.n.append('0' + str(i))
                else:
                    self.n.append(str(i))
        self.count = 1
        self.month.values = self.n

    def get_hour(self):
        if self.count == 0:
            for i in range(1, 24):
                if i < 10:
                    self.n.append('0' + str(i))
                else:
                    self.n.append(str(i))
        self.count = 1
        self.hour.values = self.n

    def get_minute(self):
        if self.count == 0:
            for i in range(1, 60):
                if i < 10:
                    self.n.append('0' + str(i))
                else:
                    self.n.append(str(i))
        self.count = 1
        self.minute.values = self.n


# ---------------------------------------------------#

# mainApp class
class mainApp(App):
    time = StringProperty()

    def update(self, *args):
        self.time = str(time.asctime())

    def build(self):
        self.title = "Calendar"
        self.load_kv('CalendarScreen.kv')
        Clock.schedule_interval(self.update, 1)
        return CalendarScreen()


if __name__ == '__main__':
    app = mainApp()
    app.run()
