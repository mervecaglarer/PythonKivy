from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
Builder.load_string("""
<GirisEkrani>:
    GridLayout:
        rows:3
        cols:2
        Label:
            text: "Add event:"
            font_size: "20sp"
        TextInput:
            id: event
            multiline: False
        Label:
            text: "What is deadline:"
            font_size: "20sp"
        TextInput:
            id: deadline
            multiline: False
        Button:
            text: "finish"
            on_press:root.GirisEkrani()
        Button:
            text: "next"
            on_press: root.login()

<GirisOnayEkrani>:
    karsilama_yazisi: karsilama_yazisi
    BoxLayout:
        id: kutu
        orientation: "vertical"
        Label:
            id: karsilama_yazisi
            text: "welcome"

<GirisRedEkrani>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: "add different event"
            on_press: root.anaEkranaDon()

<RootWidget>:
    id: kok
    GirisEkrani:
        id: giris
        name: "giris_ekrani"
    GirisOnayEkrani:
        id: onay
        name: "giris_basarili"
    GirisRedEkrani:
        id: red
        name: "giris_hatali"
""")
class GirisEkrani(Screen):
    pass

class GirisOnayEkrani(Screen):
    def on_stop(self):
        pass

class GirisRedEkrani(Screen):
    def anaEkranaDon(self):
        self.manager.current = "giris_ekrani"

class RootWidget(ScreenManager):
    pass

class todolistApp(App):
    def build(self):
        self.title="ToDoList"
        return RootWidget()

if __name__ == "__main__":
    todolistApp().run()