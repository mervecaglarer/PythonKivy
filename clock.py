from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.lang import Builder

Builder.load_string("""
<RootWidget>:
    orientation: "vertical"
    Label:
        id: hello_text
        text: str(root.counter)
        font_size: "50sp"
    Label:
        id: my_text
        text: "Clock"
    Button:
        text: "Start"
        on_press: my_text.text = root.startCounter()
    Button:
        text: "Pause"
        on_press: my_text.text = root.pauseCounter()
    Button:
        text: "Reset"
        on_press: my_text.text = root.resetCounter()
""")
class RootWidget(BoxLayout):
    counter = NumericProperty(0)
    counting = False
    
    def startCounter(self):
        if not self.counting:
            Clock.schedule_interval(self.resetsecond, 1)
            self.counting = True
            return "Started"
        else:
            return "Already started"

    def pauseCounter(self):
        Clock.unschedule(self.resetsecond)
        self.counting = False
        return "Paused"

    def resetCounter(self):
        self.secondzero()
        return "Stopped"

    def resetsecond(self, dt):
        print (self.counter)
        self.counter += 1

    def secondzero(self):
        self.counter = 0


class clockApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    clockApp().run()
