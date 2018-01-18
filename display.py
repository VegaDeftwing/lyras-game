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
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

class LyraGame(Widget):
    # def update(self, dt):
        #print(dt)
    pass


class LyraApp(App):
    def build(self):
        display = LyraGame()
        # Clock.schedule_interval(display.update, 1.0 / 60.0)
        return display



LyraApp().run()
