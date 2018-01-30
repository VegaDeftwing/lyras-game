from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, StringProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.lang import Builder
import buttons

class BtnLayout(GridLayout):
    def __init__(self, **kwargs):
        super(BtnLayout, self).__init__(**kwargs)
        btnlst = buttons.makebtns(15)
        btnlst[1].bind(on_press=self.clk)
        btnlst[1].text = "test"
        for x in range(0, 15):
            self.add_widget(btnlst[x])

    def clk(self, obj):
        print("Button Pressed")

class FinalLayout(Widget):
    display_text = StringProperty("hem")
    def __init__(self, **kwargs):
        super(FinalLayout, self).__init__(**kwargs)
        self.display_text = "testtest testtest testtest"
    def update(self, dt):
        self.display_text = "fucking please"

class Lyra2App(App):
    def build(self):
        display = FinalLayout()
        Clock.schedule_interval(display.update, 1.0 / 60.0)
        return display


Lyra2App().run()
