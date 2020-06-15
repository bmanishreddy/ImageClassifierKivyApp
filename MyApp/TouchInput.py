import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class Touch(Widget):
    btn = ObjectProperty()

    def on_touch_down(self, touch):
        print("Mouse Down",touch)
        self.btn.opacity = 0.5



    def on_touch_move(self, touch):
        print("Mouse move ",touch)
        pass
    def on_touch_up(self, touch):
        print("Mouse up ",touch)
        pass

class TouchApp(App):
    def build(self):
        return Touch()


if __name__  == "__main__":
    TouchApp().run()