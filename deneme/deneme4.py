from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.lang import Builder

Builder.load_string("""
<metinDuzenleyici>:
    BoxLayout:
        orientation: "vertical"
        exit_on_escape:False
        TextInput:
            size_hint_y: 90
            id: metin
            multiline:True
        BoxLayout:
            size_hint_y: 10
            Button:
                text: "Aç"
                on_press:pass
            Button:
                text: "Kaydet"
                on_press:pass
            Button:
                text: "Farklı Kaydet"
                on_press:pass
            Button:
                text: "Yeni"
                on_press:pass
<farkliKaydetForm>:
    title: "Dosya Kaydet"
    size_hint: (.9, .9)
    BoxLayout:
        orientation: 'vertical'
        FileChooserListView:
            size_hint_y: 80
            id: dosya_secim
            filters: ['*.*']
            path: app.son_patika
            on_selection:pass
        BoxLayout:
            size_hint_y: 10
            Label:
                text: "Dosya Adı:"
                size_hint_x: 20
            TextInput:
                id: dosya_adi
                size_hint_x: 80
        BoxLayout:
            size_hint_y: 10
            Button:
                text: "Kaydet"
                on_press:pass
            Button:
                text: "Vazgeç"
                on_press: root.dismiss()
""")

class farkliKaydetForm(Popup):
    pass
class RootWidget(ScreenManager):
    pass

class metinDuzenleyici(App):
    def build(self):
        return RootWidget()

metinDuzenleyici().run()