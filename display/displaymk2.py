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
        btnlst[1].text = "test"
        for x in range(0, 15):
            btnstring = "test " + str(x)
            btnlst[x].text = btnstring
            btnlst[x].bind(on_press=self.clk)
            self.add_widget(btnlst[x])

    def clk(self, obj):
        print(str(obj.text) + ": Button Pressed")
        FinalLayout.update(self,1)

class FinalLayout(Widget):
    text = StringProperty("testtest")
    def __init__(self, **kwargs):
        super(FinalLayout, self).__init__(**kwargs)
        self.text = "If you are seeing this something has gone very, very wrong. May the debugging gods take pitty on you."
    def update(self, dt):
        self.text = "Please fucking work"

class Lyra2App(App):
    def build(self):
        display = FinalLayout()
        Clock.schedule_interval(display.update, 1.0 / 60.0)
        return display


Lyra2App().run()
