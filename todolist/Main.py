from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import json

file = open("data")
file_read=file.read()
file_data=json.loads(file_read)
arr=[]
for x in file_data:
    arr.append(x)

Builder.load_string("""
<MenuScreen>:
    GridLayout:
        cols:2
        padding: 3
        spacing: 3
        GridLayout:
            cols:2
            Label:
                text:"write event:"
            TextInput:
                id:adding
                multiline:False
            Label:
                text:"deadline:"
            TextInput:
                id:deadline
                multiline:False
       
        Button:
            text: 'add'
            font_size: 20
            on_press:
                root.add()
                root.manager.current = 'add'
            
        Button:
            text: 'List'
            font_size: 40
            on_press: root.manager.current = 'list'
        

<ListScreen>:
    BoxLayout:
        Button:
            text: 'go back'
            on_press: root.manager.current = 'menu'
      

""")


class MenuScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    file = open("data")
    file_read = file.read()
    file_data = json.loads(file_read)
    arr = []
    file.close()
    for i in file_data:
        arr.append(i)
    def add(self):
        task=self.ids.adding.text
        deadline=self.ids.deadline.text
        new = {"task": task, "deadline": deadline}
        arr.append(new)
        print(arr)
        with open("data","w") as outfile:
            json.dump(arr,outfile)

class ListScreen(Screen):
    pass


class AddScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ListScreen(name='list'))
sm.add_widget(AddScreen(name='add'))


class TestApp(App):
    def build(self):
        self.title = "ToDoList"
        return sm


if __name__ == '__main__':
    TestApp().run()
