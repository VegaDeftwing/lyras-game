from kivy.uix.button import Button

def setbgrs_active(btn):
    btn.background_normal = "/home/vega/Documents/GitHub/local/lyras-game/documents/button_w_shortcut.png"
    btn.background_down = "/home/vega/Documents/GitHub/local/lyras-game/documents/button_w_shortcut_pressed.png"

def setbgrs_inactive(btn):
    btn.background_normal = "/home/vega/Documents/GitHub/local/lyras-game/documents/button_inactive.png"
    btn.background_down = "/home/vega/Documents/GitHub/local/lyras-game/documents/button_inactive.png"
    btn.background_disabled_normal = "/home/vega/Documents/GitHub/local/lyras-game/documents/button_inactive.png"
    btn.text = " "
    btn.disabled = True

def setbgrs_blank(btn):
    btn.background_normal = "/home/vega/Documents/GitHub/local/lyras-game/documents/button_blank.png"
    btn.background_down = "/home/vega/Documents/GitHub/local/lyras-game/documents/button_blank.png"
    btn.background_disabled_normal = "/home/vega/Documents/GitHub/local/lyras-game/documents/button_blank.png"
    btn.text = ""
    btn.disabled = True

def makebtns(num):
    btnlst = []
    for x in range(0,num):
        btnlst.append(Button(text="", size_hint_x=None, size=(240, 75), size_hint=(None, None)))
    return btnlst
