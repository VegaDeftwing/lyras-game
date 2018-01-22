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
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

#Style/image stuff, gets defined up for fn declaration order
def setbgrs(btn):
    btn.background_normal = "/home/vega/Documents/GitHub/local/lyras-game/documents/button_w_shortcut.png"
    btn.background_down = "/home/vega/Documents/GitHub/local/lyras-game/documents/button_w_shortcut_pressed.png"

def makebtns(num):
    btnlst = []
    for x in range(0, num):
        btnlst.append(Button(text = "I'm button #{0}".format(x), size_hint_x=None, size=(240,75), size_hint=(None, None)))
        setbgrs(btnlst[x])
    return btnlst

class LyraGame(Widget):
    # def update(self, dt):
        #print(dt)
    pass

class BtnLayout(GridLayout):
    def __init__(self, row_default_height=40, **kwargs):
        super(BtnLayout, self).__init__(**kwargs)
        self.spacing = 13
        self.cols = 5
        self.rows = 3
        # btn1 = Button(text = "I'm a button!!!", size_hint_x=None, size=(240,75), size_hint=(None, None))
        # btn2 = Button(text = "I'm a button too!", size_hint_x=None, size=(240,75), size_hint=(None, None))
        # setbgrs(btn1)
        # setbgrs(btn2)
        btnlst = makebtns(15)
        # btn1.bind(on_press=self.clk)
        for x in range(0,15):
            self.add_widget(btnlst[x])
        # self.add_widget(btn1)
        # self.add_widget(btn2)
    def clk(self, obj):
        print("Button Pressed")


class LyraApp(App):
    def build(self):
        display = BtnLayout()
        # Clock.schedule_interval(display.update, 1.0 / 60.0)
        return display



LyraApp().run()
