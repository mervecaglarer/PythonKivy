from kivy.uix.screenmanager import ScreenManager


class SM(ScreenManager):
    def __init__(self, **kwargs):
        super(SM, self).__init__(**kwargs)
        self.current = "CalendarScreen"

