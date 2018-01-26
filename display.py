# This file handles writing
# to the screen and interacting with the text (scrolling)
# as well as displaying the general UI
# and will require assets to be made

# Basically I'm going to rip off trials in tainted space.
# Oops.
# LOC - ROOM#                       Day/Month/Year
#
#
#                                                   Stats
#                                   <--T->          ---x------
#                                      E            -x--------
# Rooms Drawn like TiTs                X            ------x---
#          X                           T            -x--------
#        X-X-X-X-X-X-X-                             ----x-----
#           X X     X                  H            -x--------
#                 X-X  X               E            ---------x
#                   X-X                R
#                                   <--E->
#
#   "Check" "Talk" "Act"
#   "Enter"  W
#         A  S  D "Inventory"
#

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

# Builder.load_string('''
# <ScrolllabelLabel>:
#     Label:
#         text: root.text
#         font_size: 20
#         text_size: self.width, None
#         size_hint_y: None
#         height: self.texture_size[1]
# ''')


# This is the class that produces the text view
class ScrolllabelLabel(ScrollView):
    text = StringProperty()
    def __init__(self, text, **kwargs):
        super(ScrolllabelLabel, self).__init__(**kwargs)
        self.text = str(text)
    def update(self):
        self.text = str("text")



def setbgrs(btn):
    btn.background_normal = "/home/vega/Documents/GitHub/local/lyras-game/documents/button_w_shortcut.png"
    btn.background_down = "/home/vega/Documents/GitHub/local/lyras-game/documents/button_w_shortcut_pressed.png"


def makebtns(num):
    btnlst = []
    for x in range(0, num):
        btnlst.append(Button(text="I'm button #{0}".format(x), size_hint_x=None, size=(240,75), size_hint=(None, None)))
        setbgrs(btnlst[x])
    return btnlst


def makemap(num):
    imglst = []
    for x in range(0, 13):
        imglst.append(Image(source="/home/vega/Documents/GitHub/local/lyras-game/documents/mapbase_X.png"))
        imglst.append(Image(source="/home/vega/Documents/GitHub/local/lyras-game/documents/mapbase_oneside.png"))
        imglst.append(Image(source="/home/vega/Documents/GitHub/local/lyras-game/documents/mapbase_T.png"))
        imglst.append(Image(source="/home/vega/Documents/GitHub/local/lyras-game/documents/mapbase_line.png"))

    imglst.append(Image(source="/home/vega/Documents/GitHub/local/lyras-game/documents/mapbase_T.png"))
    imglst.append(Image(source="/home/vega/Documents/GitHub/local/lyras-game/documents/mapbase_line.png"))
    return imglst


class Map(GridLayout):
    def __init__(self, **kwargs):
        super(Map, self).__init__(**kwargs)
        self.cols = 9
        self.rows = 6
        self.padding = (5, 7)
        imglst = makemap(54)
        for x in range(0, 54):
            self.add_widget(imglst[x])
            imglst[x].height = 200
            imglst[x].width = 200



class Stats():
    def __init__(self, **kwargs):
        super(Stats, self).__init__(**kwargs)


class StatsAndMap(GridLayout):
    def __init__(self, **kwargs):
        super(StatsAndMap, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 2
        a = Button()
        b = Map()
        self.add_widget(a)
        self.add_widget(b)


class CharsAndMenu(GridLayout):
    def __init__(self, **kwargs):
        super(CharsAndMenu, self).__init__(**kwargs)


class BtnLayout(GridLayout):
    def __init__(self, **kwargs):
        super(BtnLayout, self).__init__(**kwargs)
        self.spacing = 13
        self.cols = 5
        self.rows = 3
        self.height = 270
        btnlst = makebtns(15)
        btnlst[1].bind(on_press=self.clk)
        btnlst[1].text = "test"
        for x in range(0, 15):
            self.add_widget(btnlst[x])
        # self.add_widget(btn1)
        # self.add_widget(btn2)

    def clk(self, obj):
        print("Button Pressed")


class FinalLayout(GridLayout):
    b = ScrolllabelLabel("a")
    def __init__(self, **kwargs):
        super(FinalLayout, self).__init__(**kwargs)
        self.rows = 2
        self.cols = 2
        # Stats
        a = StatsAndMap()
        b = ScrolllabelLabel("test")
        c = CharsAndMenu()
        b.size_hint = (2.2, 3)
        # Blank, for text Win cont
        d = BtnLayout()
        # c2r2.size_hint = (.66, 0.5)
        self.add_widget(a)
        self.add_widget(b)
        self.add_widget(c)
        self.add_widget(d)


class LyraApp(App):
    def build(self):
        display = FinalLayout()
        # display = ScrolllabelLabel()
        # Clock.schedule_interval(display.b.update(), 1.0 / 60.0)
        return display


LyraApp().run()
