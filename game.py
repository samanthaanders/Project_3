import random
#import player
#import enemy

class player:
    def __init__(self, name, strength, health):
        self.name = name
        self.strength = strength
        self.health = health
    def take_damage(self, damage):
        self.health -= damage

class enemy:
    def __init__(self, strength, health, num):
        self.strength = strength
        self.health = health
        self.num = num
    def take_damage(self, num, damage):
        if (damage == self.num):
            self.health -= damage
        elif (self.num - damage == 1):
            self.health -= damage / 2


name = input("what is your name? \n")
p1 = player(name, 5, 10)
print ("hello,",p1.name)

e1 = enemy(8, 10, (random.randint(0,5)))

p1.take_damage(e1.strength)
print("your health is now ", p1.health)

attack = input("input a number \n")

e1.take_damage(int(attack), (p1.strength))
print(e1.num)
print(e1.health)
