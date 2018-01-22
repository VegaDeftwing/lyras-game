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


class ScrolllabelLabel(ScrollView):
    text = StringProperty("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque ac scelerisque eros. In et pretium ipsum, molestie consectetur dolor. Suspendisse facilisis eleifend consectetur. Etiam nec justo non sem viverra finibus eget sed purus. Aliquam ac erat tellus. In sit amet velit eget turpis consectetur molestie in in ex. Morbi auctor blandit tortor non lobortis. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus tempus purus nisl, in pulvinar dui sagittis vel. Donec sed bibendum est. Donec ante justo, elementum non erat eu, volutpat elementum sem. Aliquam convallis, tortor quis auctor viverra, sapien dolor sollicitudin sem, accumsan malesuada enim ante sed ipsum. Praesent maximus gravida velit non egestas. Proin ac egestas turpis, eu semper tellus. Suspendisse eget luctus nisl. Suspendisse potenti. Cras eu tincidunt lacus. Donec non nisi consectetur, suscipit nunc eget, tempor risus. Pellentesque tincidunt luctus augue non tempus. Nam ac nisi risus. Vestibulum faucibus lobortis vehicula. Nulla vel sem ante. Etiam pellentesque aliquet fermentum. Morbi pretium, sem et mollis sagittis, lectus odio condimentum nibh, et efficitur libero lectus sit amet erat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Morbi et neque nec justo aliquet accumsan et ut sem. Proin justo nulla, laoreet sit amet velit a, auctor scelerisque tortor. Aliquam at fermentum ante, non suscipit ipsum. Vivamus elementum libero ut nunc ullamcorper, ac cursus libero faucibus. Donec eu convallis leo. Mauris ac tempus lacus. Morbi ac metus ultrices, commodo odio non, malesuada ex. Ut nec lobortis elit, sed facilisis risus. Sed vitae enim mi. Nunc eget arcu tincidunt, tristique lacus ut, tincidunt justo. Donec varius vestibulum augue non scelerisque. Donec maximus mollis sodales. Suspendisse faucibus, felis ornare fringilla accumsan, nisl eros lobortis nisl, cursus faucibus felis nulla scelerisque quam. Nulla euismod orci et nisi vestibulum, quis facilisis dolor consectetur. Sed vestibulum pulvinar sapien sit amet cursus. Duis et egestas velit. Cras tempus quam quis ex scelerisque, quis fringilla velit fermentum. Nulla aliquet faucibus ante sed maximus. Aenean tristique non leo eget feugiat. In hac habitasse platea dictumst. Nunc dictum dolor eu luctus aliquam. Phasellus tincidunt fermentum orci, ut dictum ex eleifend sed. Curabitur lacinia id nunc vitae feugiat. Praesent eu maximus massa. Cras auctor semper turpis, ac ornare enim consequat a. Quisque in sodales massa. Donec gravida lorem et fringilla sodales. Ut sit amet iaculis quam. Mauris porttitor nulla magna. Morbi ut justo convallis, laoreet diam vitae, blandit est. Nullam id turpis eleifend, efficitur nunc ut, lacinia tellus. Nam ut elementum eros. Fusce tincidunt lacus nunc. Donec venenatis maximus justo, et porttitor lectus ullamcorper finibus. Aliquam in velit non massa dictum vehicula eget at orci. Praesent blandit pretium enim, vel interdum leo vehicula vitae. In pellentesque sed mauris ut ultrices.Duis aliquam nisi nibh, eget volutpat ipsum commodo ac. Nulla facilisi. Nam vel tincidunt tellus, eu ullamcorper tellus. Phasellus tincidunt quis dolor in volutpat. In nunc nisi, congue eget imperdiet a, malesuada et mi. Aenean ac eros semper, pulvinar dolor nec, aliquet nulla. Quisque porttitor urna sed orci tincidunt sagittis. Cras sed ex dui. Cras hendrerit mauris ipsum, a dictum augue viverra sit amet. Fusce luctus ultrices magna eget venenatis. Cras hendrerit et risus sollicitudin consequat. Nam sed neque neque.Duis aliquam nisi nibh, eget volutpat ipsum commodo ac. Nulla facilisi. Nam vel tincidunt tellus, eu ullamcorper tellus. Phasellus tincidunt quis dolor in volutpat. In nunc nisi, congue eget imperdiet a, malesuada et mi. Aenean ac eros semper, pulvinar dolor nec, aliquet nulla. Quisque porttitor urna sed orci tincidunt sagittis. Cras sed ex dui. Cras hendrerit mauris ipsum, a dictum augue viverra sit amet. Fusce luctus ultrices magna eget venenatis. Cras hendrerit et risus sollicitudin consequat. Nam sed neque neque.Duis aliquam nisi nibh, eget volutpat ipsum commodo ac. Nulla facilisi. Nam vel tincidunt tellus, eu ullamcorper tellus. Phasellus tincidunt quis dolor in volutpat. In nunc nisi, congue eget imperdiet a, malesuada et mi. Aenean ac eros semper, pulvinar dolor nec, aliquet nulla. Quisque porttitor urna sed orci tincidunt sagittis. Cras sed ex dui. Cras hendrerit mauris ipsum, a dictum augue viverra sit amet. Fusce luctus ultrices magna eget venenatis. Cras hendrerit et risus sollicitudin consequat. Nam sed neque neque. Duis aliquam nisi nibh, eget volutpat ipsum commodo ac. Nulla facilisi. Nam vel tincidunt tellus, eu ullamcorper tellus. Phasellus tincidunt quis dolor in volutpat. In nunc nisi, congue eget imperdiet a, malesuada et mi. Aenean ac eros semper, pulvinar dolor nec, aliquet nulla. Quisque porttitor urna sed orci tincidunt sagittis. Cras sed ex dui. Cras hendrerit mauris ipsum, a dictum augue viverra sit amet. Fusce luctus ultrices magna eget venenatis. Cras hendrerit et risus sollicitudin consequat. Nam sed neque neque.Duis aliquam nisi nibh, eget volutpat ipsum commodo ac. Nulla facilisi. Nam vel tincidunt tellus, eu ullamcorper tellus. Phasellus tincidunt quis dolor in volutpat. In nunc nisi, congue eget imperdiet a, malesuada et mi. Aenean ac eros semper, pulvinar dolor nec, aliquet nulla. Quisque porttitor urna sed orci tincidunt sagittis. Cras sed ex dui. Cras hendrerit mauris ipsum, a dictum augue viverra sit amet. Fusce luctus ultrices magna eget venenatis. Cras hendrerit et risus sollicitudin consequat. Nam sed neque neque.Duis aliquam nisi nibh, eget volutpat ipsum commodo ac. Nulla facilisi. Nam vel tincidunt tellus, eu ullamcorper tellus. Phasellus tincidunt quis dolor in volutpat. In nunc nisi, congue eget imperdiet a, malesuada et mi. Aenean ac eros semper, pulvinar dolor nec, aliquet nulla. Quisque porttitor urna sed orci tincidunt sagittis. Cras sed ex dui. Cras hendrerit mauris ipsum, a dictum augue viverra sit amet. Fusce luctus ultrices magna eget venenatis. Cras hendrerit et risus sollicitudin consequat. Nam sed neque neque.Duis aliquam nisi nibh, eget volutpat ipsum commodo ac. Nulla facilisi. Nam vel tincidunt tellus, eu ullamcorper tellus. Phasellus tincidunt quis dolor in volutpat. In nunc nisi, congue eget imperdiet a, malesuada et mi. Aenean ac eros semper, pulvinar dolor nec, aliquet nulla. Quisque porttitor urna sed orci tincidunt sagittis. Cras sed ex dui. Cras hendrerit mauris ipsum, a dictum augue viverra sit amet. Fusce luctus ultrices magna eget venenatis. Cras hendrerit et risus sollicitudin consequat. Nam sed neque neque.Duis aliquam nisi nibh, eget volutpat ipsum commodo ac. Nulla facilisi. Nam vel tincidunt tellus, eu ullamcorper tellus. Phasellus tincidunt quis dolor in volutpat. In nunc nisi, congue eget imperdiet a, malesuada et mi. Aenean ac eros semper, pulvinar dolor nec, aliquet nulla. Quisque porttitor urna sed orci tincidunt sagittis. Cras sed ex dui. Cras hendrerit mauris ipsum, a dictum augue viverra sit amet. Fusce luctus ultrices magna eget venenatis. Cras hendrerit et risus sollicitudin consequat. Nam sed neque neque.Duis aliquam nisi nibh, eget volutpat ipsum commodo ac. Nulla facilisi. Nam vel tincidunt tellus, eu ullamcorper tellus. Phasellus tincidunt quis dolor in volutpat. In nunc nisi, congue eget imperdiet a, malesuada et mi. Aenean ac eros semper, pulvinar dolor nec, aliquet nulla. Quisque porttitor urna sed orci tincidunt sagittis. Cras sed ex dui. Cras hendrerit mauris ipsum, a dictum augue viverra sit amet. Fusce luctus ultrices magna eget venenatis. Cras hendrerit et risus sollicitudin consequat. Nam sed neque neque. Duis aliquam nisi nibh, eget volutpat ipsum commodo ac. Nulla facilisi. Nam vel tincidunt tellus, eu ullamcorper tellus. Phasellus tincidunt quis dolor in volutpat. In nunc nisi, congue eget imperdiet a, malesuada et mi. Aenean ac eros semper, pulvinar dolor nec, aliquet nulla. Quisque porttitor urna sed orci tincidunt sagittis. Cras sed ex dui. Cras hendrerit mauris ipsum, a dictum augue viverra sit amet. Fusce luctus ultrices magna eget venenatis. Cras hendrerit et risus sollicitudin consequat. Nam sed neque neque. Duis aliquam nisi nibh, eget volutpat ipsum commodo ac. Nulla facilisi. Nam vel tincidunt tellus, eu ullamcorper tellus. Phasellus tincidunt quis dolor in volutpat. In nunc nisi, congue eget imperdiet a, malesuada et mi. Aenean ac eros semper, pulvinar dolor nec, aliquet nulla. Quisque porttitor urna sed orci tincidunt sagittis. Cras sed ex dui. Cras hendrerit mauris ipsum, a dictum augue viverra sit amet. Fusce luctus ultrices magna eget venenatis. Cras hendrerit et risus sollicitudin consequat. Nam sed neque neque. Duis aliquam nisi nibh, eget volutpat ipsum commodo ac. Nulla facilisi. Nam vel tincidunt tellus, eu ullamcorper tellus. Phasellus tincidunt quis dolor in volutpat. In nunc nisi, congue eget imperdiet a, malesuada et mi. Aenean ac eros semper, pulvinar dolor nec, aliquet nulla. Quisque porttitor urna sed orci tincidunt sagittis. Cras sed ex dui. Cras hendrerit mauris ipsum, a dictum augue viverra sit amet. Fusce luctus ultrices magna eget venenatis. Cras hendrerit et risus sollicitudin consequat. Nam sed neque neque. Duis aliquam nisi nibh, eget volutpat ipsum commodo ac. Nulla facilisi. Nam vel tincidunt tellus, eu ullamcorper tellus. Phasellus tincidunt quis dolor in volutpat. In nunc nisi, congue eget imperdiet a, malesuada et mi. Aenean ac eros semper, pulvinar dolor nec, aliquet nulla. Quisque porttitor urna sed orci tincidunt sagittis. Cras sed ex dui. Cras hendrerit mauris ipsum, a dictum augue viverra sit amet. Fusce luctus ultrices magna eget venenatis. Cras hendrerit et risus sollicitudin consequat. Nam sed neque neque. Duis aliquam nisi nibh, eget volutpat ipsum commodo ac. Nulla facilisi. Nam vel tincidunt tellus, eu ullamcorper tellus. Phasellus tincidunt quis dolor in volutpat. In nunc nisi, congue eget imperdiet a, malesuada et mi. Aenean ac eros semper, pulvinar dolor nec, aliquet nulla. Quisque porttitor urna sed orci tincidunt sagittis. Cras sed ex dui. Cras hendrerit mauris ipsum, a dictum augue viverra sit amet. Fusce luctus ultrices magna eget venenatis. Cras hendrerit et risus sollicitudin consequat. Nam sed neque neque. END TEST")


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
    def __init__(self, **kwargs):
        super(FinalLayout, self).__init__(**kwargs)
        self.rows = 2
        self.cols = 2
        # Stats
        a = StatsAndMap()
        b = ScrolllabelLabel()
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
        # Clock.schedule_interval(display.update, 1.0 / 60.0)
        return display


LyraApp().run()
