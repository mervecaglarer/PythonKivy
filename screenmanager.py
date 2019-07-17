from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.network.urlrequest import UrlRequest

Builder.load_string("""
<GirisEkrani>:
    GridLayout:
        rows:3
        cols:2
        Label:
            text: "Kullanıcı adı:"
            font_size: "20sp"
        TextInput:
            id: username
            multiline: False
        Label:
            text: "Şifre:"
            font_size: "20sp"
        TextInput:
            id: passwd
            multiline: False
            password: True
        Button:
            text: "Şifremi Unuttum"
        Button:
            text: "Oturum Aç"
            on_press: root.login()

<GirisOnayEkrani>:
    karsilama_yazisi: karsilama_yazisi
    BoxLayout:
        id: kutu
        orientation: "vertical"
        Label:
            id: karsilama_yazisi
            text: "Hoşgeldiniz"

<GirisRedEkrani>:
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "Hatalı Giriş"
        Button:
            text: "Tekrar Dene"
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
    def login(self):
        if self.ids.username.text == "root" and\
            self.ids.passwd.text == "123":
            print ("dogru giris")
            self.manager.current = "giris_basarili"
            istek = UrlRequest("http://api.openweathermap.org/data/2.1/find/city?lat=41.0053215&lon=29.0121795&cnt=1", self.incomingData)
        else:
            print ("sifre yanlis")
            self.manager.current = "giris_hatali"

    def incomingData(self, req, results):
        print (results)
        data = eval(results)
        sicaklik = data["list"][0]["main"]["temp"]-273.15
        print (sicaklik)
        self.parent.ids.onay.karsilama_yazisi.text = str(sicaklik) + " derece"

class GirisOnayEkrani(Screen):
    pass

class GirisRedEkrani(Screen):
    def anaEkranaDon(self):
        self.manager.current = "giris_ekrani"

class RootWidget(ScreenManager):
    pass

class GirisSistemiApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    GirisSistemiApp().run()
