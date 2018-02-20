import character
import time


def clear():
    print(chr(27) + "[2J")
    time.sleep(.05)

def makereal(layout):
    #clear()
    # firstName = input("What is your REAL first name?\n")
    layout.text = "What is your REAL first name?"
    # make text box, sanatize to capital first and check if one word
    layout.text = "What is your REAL last name?"
    # make text box, sanatize to capital first and check if one word
    layout.text = "In real life how old are you? [any value under 16 will be changed to 16]"
    # check that entry is numeric, check that it is at least 16 and under 100. If not ask for reentry
    layout.text = "What is your REAL height? [in inches]"
    # check that entry is numeric. Print out height converted to x'y" and confirm
    layout.text = "What is your REAL weight? [in lbs]"
    # check that entry is above 60 and bellow 800
    layout.text = "What is your REAL sexual orientation?"
    # [hetro, homo, bi, pan, ace]
    layout.text = "What is your REAL your job title? ex: Lawyer, Lumberjack, Programmer, etc."
    # respond with so you are a _ after, to make sure the grammer is ok?
    layout.text = "Are you a virgin in REAL life?"
    # Yes, No
    layout.text = "In REAL life, on a scale from 0 to 100 how liberal [0] or conservative [100] are you?"
    # Text entry, sanatize to scale
    layout.text = "In REAL life, On a scale from 0 to 100 how libertarian [0] or authoritarian [100] are you?"
    # Text entry, sanatize to scale
    layout.text = "In REAL life, On a scale from 0 to 100 how law obeying are you? [0 not at all, 100 always]"
    # Text entry, sanatize to scale
    layout.text = "In REAL life, What is your gender?"
    # Male Female NonBinary

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
    # Make species prompt display info on hover
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
