import newgame
import load
import time
import pickle

save = load.loadgame()
# make the program save a hash of it's own save to detect tampering,
# this will be useful later

print(save + " loaded.")
time.sleep(.1)
# if save file is empty:
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
with open(save, 'rb') as input:
    save_data = pickle.load(input)

print(save_data)
