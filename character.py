import datetime
import random
random.seed()


class real:
    def __init__(self, firstName, lastName, height, weight,
                 sexualOrientation, occupation, virginity,
                 politicalLR, politicalLA, lawObeying, gender, age):
        self.firstName = firstName
        self.age = age
        self.lastName = lastName
        self.name = firstName + " " + lastName
        self.height = int(height)
        self.weight = int(weight)
        self.sexualOrientation = sexualOrientation
        self.occupation = occupation
        self.virginity = virginity
        self.gender = gender
        self.timePlayed = 0
        self.timeAsReal = 0
        self.politicalLR = int(politicalLR)
        self.politicalLA = int(politicalLA)
        self.lawObeying = int(lawObeying)


class user:
    def __init__(self, firstName, lastName, height, species, weight,
                 sexualOrientation, politicalLR, politicalLA, gender):
        self.firstName = firstName
        self.lastName = lastName
        self.name = firstName + " " + lastName
        # truncate name if name to 3 chars is greater than 7 chars
        if len(firstName) >= 7:
            self.nick = firstName[0] + firstName[1] + firstName[2]
        self.height = int(height) + random.randint(-10, 10)
        self.weight = int(weight) + random.randint(-20, 20)
        self.species = species
        self.race
        self.impatient = 50 + random.randint(-10, 10)
        self.lazy = 50 + random.randint(-10, 10)
        self.honesty = 50 + random.randint(-10, 10)
        self.location = "room1"
        self.health = 50 + random.randint(-10, 10)
        self.stregnth = 50 + random.randint(-10, 10)
        self.speed = 50 + random.randint(-10, 10)
        self.intel = 50 + random.randint(-10, 10)
        self.mana = 50 + random.randint(-10, 10)
        self.mental = 50 + random.randint(-30, 10)
        self.fear = 50 + random.randint(-10, 30)
        self.ego = 50 + random.randint(-10, 10)
        self.anxiety = 50 + random.randint(-10, 10)
        self.courage = 50 + random.randint(-10, 30)
        self.anger = 50 + random.randint(-10, 30)
        # Character starts sleeping
        self.sleeping = True
        self.hunger = 0.0
        self.starving = False
        self.thirst = 0.0
        self.thirsty = False
        self.sexualfrustration = 0.0 + random.randint(0, 100)
        self.timeAsUser = 0
        self.sexualOrientation = ""
        self.virginity = bool(random.getrandbits(1))
        self.politicalLR = 0.0
        self.politicalLA = 0.0
        self.dead = False
        self.lawObeying = 50 + random.randint(-25, 25)
        self.HeartRate = 60
        # Game starts at current date
        self.Year = datetime.date.today()
        self.gender = gender
