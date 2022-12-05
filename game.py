import random
import time

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
    def use_power(self, uses):
        if (self.power == "strength potion"):
            if uses > 0:
                self.strength += 5
                print(self.name +"'s strength:", self.strength)
                print(self.power +" uses left: ",(uses - 1))
            else:
                print(self.power + " has been used up")
        elif (self.power == "health potion"):
            if uses > 0:
                self.health += 5
                print(self.name +"'s health:", self.health)
                print(self.power +" uses left: ",(uses - 1))
            else:
                print(self.power + " has been used up")
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
    def __init__(self, name, cost, uses, desc):
        self.name = name
        self.cost = cost
        self.uses = uses
        self.desc = desc

name = input("what is your name? \n")
p1 = player(name, 5, 10, random.randint(1,4),0, None)
e1 = enemy("cave monster", 3, 5, (random.randint(1,4)), 3, 1)
e2 = enemy("some guy", 5, 5, (random.randint(1,4)), 9, 3)
e3 = enemy("monster", 5, 10, (random.randint(1,4)), 15, 5)
boss = enemy("big monster", 8, 15, (random.randint(1,4)), 50, 10)
strength_potion = item("strength potion", 10, 1, "increases strength by 5. Can be used once.")
health_potion = item("health potion", 8, 3, "increases health by 5. Can be used 3 times.")

print ("hello,",p1.name)
print("Type 'attack' to attack. Type 'quit' to quit the game.")
 
battling = True

def battle(e, power):
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
            p1.use_power(power.uses)
            power.uses -= 1
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

battle(e1, "")
print(" ")
print("battle 2")
time.sleep(1.5)
battle(e2, "")
print(" ")
print("battle 3")
time.sleep(1.5)
battle(e3, "")
print(" ")
ans = input("do you want to enter the shop? \n")
shop_items = [strength_potion, health_potion]
if (ans == "yes"):
    print("you have:", p1.money,"coins")
    for x in shop_items:
        print(x.name,"costs: ",x.cost, "  Description: ", x.desc)
    ans = input("which one do you want to buy? \n")
    for x in shop_items:
        if (ans == x.name):
            if (p1.money >= x.cost):
                p1.power = x.name
                print("purchaced", x.name)
                print("type '",p1.power,"' during a battle to use your item.")
            else:
                print("you do not have enough money!")
print(p1.name, "exited the shop.")
        
print(" ")
print("final battle")
if p1.power == strength_potion.name:
    battle(boss, strength_potion)
elif p1.power == health_potion.name:
    battle(boss, health_potion)
else:
    battle(boss, None)