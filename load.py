import os
import newgame
import time
import pickle
import display

def save_object(obj, filename):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def file_exists(fpath):
    if os.path.isfile(fpath) == 1:
        # print(fpath + " is [OK]")
        return False
    else:
        return True


def loadgamedisplay(layout):
    layout.text = "Please Select a Save file"
    if file_exists("./save1"):
        open("./save1", "w+")
        #print("save1 regened")
    if file_exists("./save2"):
        open("./save2", "w+")
        #print("save2 regened")
    if file_exists("./save3"):
        open("./save3", "w+")
        #print("save3 regened")
    layout.children[0].children[0].children[14].text = "blank"
    layout.children[0].children[0].children[13].text = "Save1"
    layout.children[0].children[0].children[12].text = "Save2"
    layout.children[0].children[0].children[11].text = "Save3"
    for x in range(0,11):
        layout.children[0].children[0].children[x].text = "blank"


def loadgameinput(btnpress):
    profile = btnpress
    profile = profile[4]
    gameloaded = False
    while gameloaded is False:
        if profile == '1':
            save = "./save1"
            gameloaded = True
        elif profile == '2':
            save = "./save2"
            gameloaded = True
        elif profile == '3':
            save = "./save2"
            gameloaded = True
        else:
            print("please enter a valid profile number!")
            gameloaded = False
    # return save
    print("Game Loaded")
    print(save)
    if os.stat(save).st_size == 0:
        real = newgame.makereal()
        user = newgame.makeuser(real)
        print(real)
        print("---\n")
        print(user)
        save_data = [user, real]
        load.save_object(save_data, save)
    with open(save, 'rb') as input:
        save_data = pickle.load(input)
        user = save_data[0]
        real = save_data[1]


# save = loadgame()
# make the program save a hash of it's own save to detect tampering,
# this will be useful later
# print(save.name + " loaded.")
# for line in save:
#     print(line)
