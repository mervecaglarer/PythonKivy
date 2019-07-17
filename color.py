from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_string("""
<RootWidget>:
    orientation: 'vertical'
    slider_colors: [0.5, 0.5, 0.5]
    canvas.before:
        Color:
            rgb: root.slider_colors
        Rectangle:
            pos: root.pos
            size: root.size
    Slider:
        min: 0
        max: 1
        value: 0.5
        on_value: color_label.text = "color " + \
        str(self.value); root.slider_colors = (self.value for i in range(3))
    Label:
        id: color_label
        font_size: "50sp"
        text: "Renk 0.5"
""")
class RootWidget(BoxLayout):
    pass

class colorApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    App = colorApp()
    App.run()
