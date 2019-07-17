from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.actionbar import ActionBar
from kivy.uix.actionbar import ActionView
from kivy.uix.actionbar import ActionButton
from kivy.uix.actionbar import ActionPrevious
from kivy.lang import Builder

Builder.load_string("""
< eylemCubugu >:
    BoxLayout:
        orientation: "vertical"
        pos_hint: {'top': 1}

        ActionBar:
            ActionView:
                ActionPrevious:
                    title: "Metin Düzenleyici"
                    with_previous: False
                    app_icon: "C:\Users\Merve\PycharmProjects\PythonKivy\düzenle.jpg"
                    ActionButton:
                        text: "Aç"
                        id: ac_eylem_dugmesi
                        icon: "C:\Users\Merve\PycharmProjects\PythonKivy\aç.jpg"
                    ActionButton:
                        text: "Kaydet"
                        id: kaydet_eylem_dugmesi
                        icon: "C:\Users\Merve\PycharmProjects\PythonKivy\kaydett.jpg"
                    ActionButton:
                        text: "Farklı Kaydet"
                        id: farklı_kaydet_eylem_dugmesi
                        icon: "C:\Users\Merve\PycharmProjects\PythonKivy\save.jpg"
                    ActionButton:
                        text: "Yeni"
                        id: yeni_eylem_dugmesi
                        icon: "C:\Users\Merve\PycharmProjects\PythonKivy\ekle.jpg"
                    ActionButton:
                        text: "Çık" 
                        id: yeni_eylem_dugmesi
                        icon: "C:\Users\Merve\PycharmProjects\PythonKivy\çık.jpg"
            Label:
                text: "Ana Alan"
""")

class eylemCubugu(App):

    def build(self):
        eylemcubugu = ActionBar(pos_hint={'top': 1})

        eylemgorunumu = ActionView()
        eylemcubugu.add_widget(eylemgorunumu)

        oncekieylem = ActionPrevious(title='Eylem Çubuğu' , app_icon='C:\Users\Merve\PycharmProjects\PythonKivy\doc.jpg')
        eylemgorunumu.add_widget(oncekieylem)

        duzen = BoxLayout(orientation='vertical')
        duzen.add_widget(eylemcubugu)

        self.etiket = Label(text="Ana Alan")
        duzen.add_widget(self.etiket)

        return duzen
class eylemCubugu(App):
    def build(self):
        pass

eylemCubugu().run()