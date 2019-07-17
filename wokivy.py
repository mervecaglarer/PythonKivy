import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class Mygrid(GridLayout):
    def __init__(self,**kwargs):
        super(Mygrid,self).__init__(**kwargs)
        self.cols=2
        self.add_widget(Label(text="Name:"))
        self.name=TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Surname:"))
        self.surname = TextInput(multiline=False)
        self.add_widget(self.surname)

class Myapp(App):
    def build(self):
        return Mygrid()
Myapp().run()

