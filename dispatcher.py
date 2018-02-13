from load import loadgamedisplay

def recievelayout(Layout):
    global layout
    layout = Layout

def dispatcher(obj, state):
    if state == 0:
        layout.text = "Please select a save file:"
        layout.children[0].children[0].children[14].text = "inactive"
        layout.children[0].children[0].children[13].text = "Save1"
        layout.children[0].children[0].children[12].text = "Save2"
        layout.children[0].children[0].children[11].text = "Save3"
        for x in range(0,11):
            layout.children[0].children[0].children[x].text = "blank"
        state = 1
        return state
    if state == 1 and obj != "invalid":
        loadgamedisplay(layout,str(obj.text))
        state = 2
    return state
