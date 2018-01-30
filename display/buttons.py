from kivy.uix.button import Button

def setbgrs(btn):
    btn.background_normal = "/home/vega/Documents/GitHub/local/lyras-game/documents/button_w_shortcut.png"
    btn.background_down = "/home/vega/Documents/GitHub/local/lyras-game/documents/button_w_shortcut_pressed.png"


def makebtns(num):
    btnlst = []
    for x in range(0, num):
        btnlst.append(Button(text="I'm button #{0}".format(x), size_hint_x=None, size=(240,75), size_hint=(None, None)))
        setbgrs(btnlst[x])
    return btnlst
