import character


def makereal():
    firstName = input("What is your REAL first name?\n")
    lastName = input("What is your REAL last name?\n")
    height = input("What is your REAL height?\n")
    weight = input("What is your REAL weight?\n")
    sexualOrientation = input("What is your REAL sexual orientation?\n[hetro, homo, bi, pan, ace]\n")
    occupation = input("What is your REAL weight?\n[Please enter as the title, ex Laweyer, Lumberjack]\n")
    virginity = input("Are you a virgin?[Y/N]\n")
    politicalLA = input("On a scale from 0 to 100 how liberal [0] or conservative [100] are you?\n")
    politicalLR = input("On a scale from 0 to 100 how libertarian [0] or authoritarian [100] are you?\n")
    lawObeying = input("On a scale from 0 to 100 how law obeying are you?\n [0 not at all, 100 always]\n")
    gender = input("What is your gender?[m,f,nb]\n")

    real = character.real(firstName, lastName, height, weight,
                          sexualOrientation, occupation, virginity,
                          politicalLR, politicalLA, lawObeying, gender)
    return real


def makeuser(real):
    firstName = input("What should your character's first name be?\n")
    lastName = input("What should your character's last name be?\n")
    height = input("What is your character's height? [in inches]\n")
    weight = input("What is your character's weight? [in pounds]\n")
    species = input("What species is your character?\n [human,elf,wolf,dwarf,dragon,feline,neko,alien]\n")
    politicalLA = real.politicalLA
    politicalLR = real.politicalLR
    gender = real.gender
    sexualOrientation = real.sexualOrientation
    user = character.user(firstName, lastName, height,
                          species, weight, sexualOrientation,
                          politicalLR, politicalLA, gender)
    return user
