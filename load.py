import os
import newgame
import time
import pickle
import display


# save = load.loadgame()
# # TODO: make the program save a hash of it's own save to detect tampering,
# # this will be useful later
#

def save_object(obj, filename):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def file_exists(fpath):
    if os.path.isfile(fpath) == 1:
        # print(fpath + " is [OK]")
        return False
    else:
        return True


def loadgamedisplay(Layout,btnpress):
    global layout
    layout = Layout
    layout.text = "Please Select a Save file"
    #Regen the save files if they don't exist
    if file_exists("./save1"):
        open("./save1", "w+")
    if file_exists("./save2"):
        open("./save2", "w+")
    if file_exists("./save3"):
        open("./save3", "w+")
# def loadgameinput(btnpress):
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
            layout.text = "Something went wrong!"
            gameloaded = False
    # return save
    print("Game Loaded")
    print(save)
    layout.text = "meh"
    if os.stat(save).st_size == 0:
        #real = newgame.makereal()
        #user = newgame.makeuser(real)
        #print(real)
        print("---\n")
        #print(user)
        #save_data = [user, real]
        #load.save_object(save_data, save)
    # with open(save, 'rb') as input:
    #     save_data = pickle.load(input)
    #     user = save_data[0]
    #     real = save_data[1]
    print("testing")


# save = loadgame()
# make the program save a hash of it's own save to detect tampering,
# this will be useful later
# print(save.name + " loaded.")
# for line in save:
#     print(line)
