import random


class Person:
    def __init__(self, firstname, lastname, health, status):
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        print("Hello! My name is {} {}".format(self.firstname, self.lastname))

    def emote(self):
        emotion = random.randrange(1, 4)
        if emotion == 1:
            print("{} is happy today".format(self.firstname))
        elif emotion == 2:
            print("{} is OK today".format(self.firstname))
        else:
            print("{} is not upset today".format(self.firstname))

    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy".format(self.firstname))
        elif self.health >= 76:
            print("{} is a little tired today".format(self.firstname))
        elif self.health >= 51:
            print("{} is unwell".format(self.firstname))
        elif self.health >= 26:
            print("{} goes to the doctor".format(self.firstname))
        else:
            print("{} is unconscious".format(self.firstname))


Maria = Person("Maria", "Luz", 95, status=True)
Finn = Person("Finn", "Makkonen", 78, status=False)
Abigail = Person("Abigail", "Nguen", 43, status=False)

# print("Is {} my friend? - {}".format(Maria.firstname, Maria.status))
# print("Is {} my friend? - {}".format(Finn.firstname, Finn.status))
# print("Is {} my friend? - {}".format(Abigail.firstname, Abigail.status))

# Maria.introduce()
# Finn.introduce()
# Abigail.introduce()
#
# Maria.emote()
# Finn.emote()
# Abigail.emote()
#
# Maria.status_change()
# Finn.status_change()
# Abigail.status_change()


class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon

    def introduce(self):
        print("You are my enemy!!!")

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
        print(other.health)

    def insult(self, other):
        if other.health <= 80:
            print("{} you are tired and weak".format(other.firstname))

    def steal(self, other):
        print("Ha ha ha! {}, I have your stuff!".format(other.firstname))
        if other.status:
            other.status = False

Robotnik = Enemy('rock', 'Robotnik', 'Doe', 75, False)
Robotnik.introduce()
Robotnik.hurt(Maria)
Robotnik.insult(Finn)
Robotnik.steal(Abigail)