from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

sm = ScreenManager()

for i in range(4):
    screen = Screen(name='Title %d' % i)
    sm.add_widget(screen)

sm.current = 'Title 2'

Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Go settings'
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Quit'

<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
""")

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()
