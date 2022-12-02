import random
import time
#import player
#import enemy

class player:
    def __init__(self, name, strength, health, num, money, power):
        self.name = name
        self.strength = strength
        self.health = health
        self.num = num
        self.money = money
        self.power = power
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
    def use_power(self):
        if (self.power == "sword"):
            self.strength += 5
        elif (self.power == "health potion"):
            self.health += 5
    def attack(self):
        return random.randint(1,4)

class enemy:
    def __init__(self, name, strength, health, num, money, reward):
        self.name = name
        self.strength = strength
        self.health = health
        self.num = num
        self.money = money
        self.reward = reward
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
class item:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost



name = input("what is your name? \n")
p1 = player(name, 5, 10, random.randint(1,4),0,"")
e1 = enemy("cave monster", 3, 5, (random.randint(1,4)), 3, 1)
e2 = enemy("some guy", 5, 5, (random.randint(1,4)), 9, 3)
e3 = enemy("monster", 5, 10, (random.randint(1,4)), 15, 5)
boss = enemy("big monster", 10, 15, (random.randint(1,4)), 50, 10)
sword = item("sword", 10)
health_potion = item("health potion", 8)

print ("hello,",p1.name)
print("Type 'attack' to attack. Type 'quit' to quit the game.")
 

battling = True

def battle(e):
    p1.health = 10
    while (battling == True):
        print(" ")
        p1.take_damage(e1.attack(), e.strength, e.name)
        p1.check_health()
        
        if ((p1.health <= 0)):
            battling == False
            break

        ans = input("What do you do? \n")
        if (ans == p1.power):
            p1.use_power()
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
            print("+" , e.money, "coins")
            print(p1.name,"has", p1.money,"coins")
            p1.strength += e.reward
            print("+", e.reward, "strength") 
            print(p1.name + "'s strength:",p1.strength)
            battling == False
            break

battle(e1)
print(" ")
print("battle 2")
time.sleep(1.5)
battle(e2)
print(" ")
print("battle 3")
time.sleep(1.5)
battle(e3)
print(" ")
ans = input("do you want to enter the shop? \n")
shop_items = [sword, health_potion]
if (ans == "yes"):
    print("you have:", p1.money,"coins")
    for x in shop_items:
        print(x.name,"costs: ",x.cost)
    ans = input("which one do you want to buy? \n")
    for x in shop_items:
        if (ans == x.name):
            if (p1.money >= x.cost):
                p1.power = x.name
                print("purchaced", x.name)
                print("type '",p1.power,"' during a battle to use your item.")
            else:
                print("you do not have enough money!")
print(p1.name, "exited the shop")
        
print(" ")
print("final battle")
battle(boss)



"""""
while (battling == True):
    print(" ")
    p1.take_damage(e1.attack(), boss.strength, boss.name)
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
        boss.take_damage(p1.attack(), (p1.strength), p1.name)
        boss.check_health()
    elif (ans == "quit"):
        print("thanks for playing!")
        quit()
    else:
        print("invalid response! your turn has been skipped.")
    
    time.sleep(1.5)

    if ((e.health <= 0)):
        print("Good job!")
        p1.money += e.money
        print("+" , e.money, "coins")
        print(p1.name,"has", p1.money,"coins")
        p1.strength += e.reward
        print("+", e.reward, "strength") 
        print(p1.name + "'s strength:",p1.strength)
        battling == False
        break
"""
