import newgame
import load
import time
import display
import os
import pickle

save = load.loadgame()
# TODO: make the program save a hash of it's own save to detect tampering,
# this will be useful later

print(save + " loaded.")
time.sleep(.1)
# if save file is empty:
if os.stat(save).st_size == 0:
    real = newgame.makereal()
    user = newgame.makeuser(real)
    print(real)
    print("---\n")
    print(user)

    save_data = [
        user, real
    ]
    load.save_object(save_data, save)
# if save file has data:
else:
    with open(save, 'rb') as input:
        save_data = pickle.load(input)
    user = save_data[0]
    real = save_data[1]

print(save_data)
display()
