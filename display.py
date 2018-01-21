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

class LyraGame(Widget):
    # def update(self, dt):
        #print(dt)
    pass

class LyraLayout(GridLayout):
    def __init__(self, **kwargs):
        super(LyraLayout, self).__init__(**kwargs)
        btn = Button(text = "test")
        btn.background_normal = "/home/vega/Documents/GitHub/local/lyras-game/documents/button_normal.png"
        btn.bind(on_press=self.clk)
        self.add_widget(btn)
    def clk(self, obj):
        print("Button Pressed")



class LyraApp(App):
    def build(self):
        display = LyraLayout()
        # Clock.schedule_interval(display.update, 1.0 / 60.0)
        return display



LyraApp().run()
