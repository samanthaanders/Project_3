import random
import time
#import player
#import enemy

class player:
    def __init__(self, name, strength, health, num, money):
        self.name = name
        self.strength = strength
        self.health = health
        self.num = num
        self.money = money
    def take_damage(self, num, damage, name):
        print(name, "attacked!")
        if (num == self.num):
            self.health -= damage
            print("the attack was very strong!")
        elif (self.num - num == 1):
            self.health -= damage / 2
            print("the attack was strong")
        elif (self.num - num == 2):
            self.health -= damage / 4
            print("the attack was weak")
        else:
            print("the attack failed!")
    def check_health(self):
        if (self.health <= 0):
            print(self.name,"lost!")
        else:
            print(self.name + "'s health is: ", self.health)
    def heal(self):
        self.health += 3
    def attack(self):
        return random.randint(1,4)

class enemy:
    def __init__(self, name, strength, health, num, money):
        self.name = name
        self.strength = strength
        self.health = health
        self.num = num
        self.money = money
    def take_damage(self, num, damage, name):
        print(name, "attacked!")
        if (num == self.num):
            self.health -= damage
            print("the attack was very strong!")
        elif (self.num - num == 1):
            self.health -= damage / 2
            print("the attack was strong")
        elif (self.num - num == 2):
            self.health -= damage / 4
            print("the attack was weak")
        else:
            print("the attack failed!")

    def check_health(self):
        if (self.health <= 0):
            print(self.name,"lost!")
        else:
            print(self.name + "'s health is: ", self.health)
    def attack(self):
        return random.randint(1,4)


name = input("what is your name? \n")
p1 = player(name, 5, 10, random.randint(1,4),0)
e1 = enemy("cave monster", 3, 5, (random.randint(1,4)), 3)
e2 = enemy("some guy", 5, 5, (random.randint(1,4)), 9)

print ("hello,",p1.name)
print("Type 'attack' to attack. Type 'quit' to quit the game.")
 

battling = True

def battle(e):
    p1.health = 10
    while (battling == True):
        print(" \n")
        p1.take_damage(e1.attack(), e.strength, e.name)
        p1.check_health()
        
        if ((p1.health <= 0)):
            battling == False
            break

        ans = input("What do you do? \n")
        if (ans == "heal"):
            p1.heal()
            p1.check_health()
        elif (ans == "attack"):
            #attack = input("input a number between 1-5 \n")
            e.take_damage(p1.attack(), (p1.strength), p1.name)
            e.check_health()
        elif (ans == "quit"):
            print("thanks for playing!")
            quit()
        else:
            print("invalid response! your turn has been skipped.")
    
        time.sleep(1.5)

        if ((e.health <= 0)):
            print("Good job!")
            p1.money += e.money
            print("+" , e.money, "money")
            print(p1.name,"has", p1.money,"money")
            battling == False
            break

battle(e1)
print(" \n")
print("battle 2")
battle(e2)

