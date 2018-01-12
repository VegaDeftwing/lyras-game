import character
import time


def clear():
    print(chr(27) + "[2J")
    time.sleep(.05)

def makereal():
    clear()
    firstName = input("What is your REAL first name?\n")
    clear()
    lastName = input("What is your REAL last name?\n")
    clear()
    age = input("In real life how old are you?\n [any value under 16 will be changed to 16]\n")
    clear()
    height = input("What is your REAL height?\n")
    clear()
    weight = input("What is your REAL weight?\n")
    clear()
    sexualOrientation = input("What is your REAL sexual orientation?\n[hetro, homo, bi, pan, ace]\n")
    clear()
    occupation = input("What is your REAL weight?\n[Please enter as the title, ex Laweyer, Lumberjack]\n")
    clear()
    virginity = input("Are you a virgin?[Y/N]\n")
    clear()
    politicalLA = input("On a scale from 0 to 100 how liberal [0] or conservative [100] are you?\n")
    clear()
    politicalLR = input("On a scale from 0 to 100 how libertarian [0] or authoritarian [100] are you?\n")
    clear()
    lawObeying = input("On a scale from 0 to 100 how law obeying are you?\n [0 not at all, 100 always]\n")
    clear()
    gender = input("What is your gender?[m,f,nb]\n")
    clear()

    real = character.real(firstName, lastName, height, weight,
                          sexualOrientation, occupation, virginity,
                          politicalLR, politicalLA, lawObeying, gender,age)

    print("Name: " + real.name + "\n")
    print("Age: " + str(real.age) + "\n")
    print("Height: " + str(real.height) + " inches\n")
    print("Weight: " + str(real.weight) + " lbs.\n")
    print("Gender: " + real.gender + "\n")
    print("Virginity: " + str(real.virginity) + "\n")
    print("Sexual Orientation: " + real.sexualOrientation + "\n")
    print("Percent Liberal: " + str(real.politicalLR) + "\n")
    print("Percent Libertarian: " + str(real.politicalLA) + "\n")
    print("Percent Law Obeying: " + str(real.lawObeying) + "\n")
    time.sleep(.25)
    real_confirm = input("Is this OK? [Y/N]\n")
    if real_confirm == 'Y':
        print("\n\nInfo Saved.\n")
        time.sleep(3)
        clear()
        return real
    else:
        print("\n\nThat sucks, that's what you typed. Info Saved.\n")
        time.sleep(3)
        clear()
        return real



def makeuser(real):
    print("Some of the following values will have a random offset:\n\n")
    firstName = input("What should your character's first name be?\n")
    clear()
    lastName = input("What should your character's last name be?\n")
    clear()
    height = input("What is your character's height? [in inches]\n")
    clear()
    weight = input("What is your character's weight? [in pounds]\n")
    clear()
    species = input("What species is your character?\n [human,elf,wolf,dwarf,dragon,feline,neko,alien]\n")
    clear()
    politicalLA = real.politicalLA
    politicalLR = real.politicalLR
    gender = real.gender
    sexualOrientation = real.sexualOrientation
    user = character.user(firstName, lastName, height,
                          species, weight, sexualOrientation,
                          politicalLR, politicalLA, gender)

    print("Name: " + user.name + "\n")
    print("Height: " + str(user.height) + " inches\n")
    print("Weight: " + str(user.weight) + " lbs.\n")
    print("species: " + user.species + "\n\n")
    time.sleep(.25)
    user_confirm = input("Is this OK? [Y/N]\n")
    if user_confirm == 'Y':
        print("\n\nInfo Saved.\n")
        time.sleep(3)
        clear()
        return user
    else:
        print("\n\nThat sucks, that's what you typed. Info Saved.\n")
        time.sleep(3)
        clear()
        return user
