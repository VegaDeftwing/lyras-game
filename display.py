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
import newgame
from dispatcher import dispatcher, recievelayout
import time
import os
import pickle


state = 0


def makemap(num):
    imglst = []
    for x in range(0, num):
        imglst.append(Image(source="/home/vega/Documents/GitHub/local/lyras-game/documents/mapbase_X.png"))
    return imglst

class Map(GridLayout):
    def __init__(self, **kwargs):
        super(Map, self).__init__(**kwargs)
        self.cols = 7
        self.rows = 5
        mapsize = self.cols * self.rows
        self.padding = (5, 7)
        imglst = makemap(mapsize)
        for x in range(0, mapsize):
            self.add_widget(imglst[x])
            imglst[x].height = 200
            imglst[x].width = 200

class BtnLayout(GridLayout):
    def __init__(self, **kwargs):
        super(BtnLayout, self).__init__(**kwargs)
        btnlst = buttons.makebtns(15)
        for x in range(0, 15):
            btnlst[x].bind(on_press=self.clk)
            self.add_widget(btnlst[x])


    def clk(self, obj):
        print(str(obj.text) + ": Button Pressed")
        global state
        state = dispatcher(obj, state)


    def update(self):
        for x in self.children:
            if x.text == "blank" or x.text == "":
                buttons.setbgrs_blank(x)
            elif x.text == "inactive" or x.text == " ":
                buttons.setbgrs_inactive(x)
            else:
                buttons.setbgrs_active(x)


class FinalLayout(Widget):
    text = StringProperty("testtest")


    def __init__(self, **kwargs):
        super(FinalLayout, self).__init__(**kwargs)
        self.text = "If you are seeing this something has gone very, very wrong. May the debugging gods take pitty on you."


    def update(self, dt):
        global state
        obj = "invalid"
        state = dispatcher(obj, state)
        BtnLayout.update(self.children[0].children[0])


class LyraApp(App):
    def build(self):
        display = FinalLayout()
        recievelayout(display)
        Clock.schedule_interval(display.update, 1.0 / 60.0)
        return display


LyraApp().run()
