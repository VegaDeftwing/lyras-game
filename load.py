import os
import time
import pickle
import display


def save_object(obj, filename):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def file_exists(fpath):
    if os.path.isfile(fpath) == 1:
        print(fpath + " is [OK]")
        return False
    else:
        return True


def loadgame():
    if file_exists("./save1"):
        open("./save1", "w+")
        print("save1 regened")
    if file_exists("./save2"):
        open("./save2", "w+")
        print("save2 regened")
    if file_exists("./save3"):
        open("./save3", "w+")
        print("save3 regened")
    gameloaded = False
    time.sleep(.1)
    while gameloaded is False:
        profile = input("Chose a profile [1,2,3]\n")
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
    return save


# save = loadgame()
# make the program save a hash of it's own save to detect tampering,
# this will be useful later
# print(save.name + " loaded.")
# for line in save:
#     print(line)
