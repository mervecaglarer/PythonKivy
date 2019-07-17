import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<FirstScreen>:
    name: '_first_screen_'
    Label:
        id: first_screen
        text: "Hi I'm The First Screen"
<SecondScreen>:
    name: '_second_screen_'
    Label:
        id: second_screen
        text: "Hi I'm The Second Screen"
<ThirdScreen>:
    name: '_third_screen_'
    Label:
        id: third_screen
        text: "Hi I'm The Third Screen"
<FourthScreen>:
    name: '_fourth_screen_'
    Label:
        id: fourth_screen
        text: "Hi I'm The Fourth Screen"
""")

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class ThirdScreen(Screen):
    pass

class FourthScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(FirstScreen())
sm.add_widget(SecondScreen())
sm.add_widget(ThirdScreen())
sm.add_widget(FourthScreen())

class SwitchingScreenApp(App):
    def build(self):
        Clock.schedule_once(self.screen_switch_one, 2)
        Clock.schedule_once(self.screen_switch_two, 4)
        Clock.schedule_once(self.screen_switch_three, 6)
        Clock.schedule_once(self.screen_switch_four, 8)
        Clock.schedule_once(self.screen_switch_one, 10)
        return sm

    def screen_switch_one(a,b):
        sm.current = '_first_screen_'
    def screen_switch_two(a,b):
        sm.current = '_second_screen_'
    def screen_switch_three(a,b):
        sm.current = '_third_screen_'
    def screen_switch_four(a,b):
        sm.current = '_fourth_screen_'

SwitchingScreenApp().run()