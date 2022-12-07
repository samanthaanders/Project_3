import random
import time

class player:
    def __init__(self, name, strength, health, num, money, power):
        self.name = name
        self.strength = strength
        self.health = health
        self.num = num # used for randomizing damage dealt in attacks
        self.money = money
        self.power = power
    def take_damage(self, num, damage, name):
        print(name, "attacked!")
        if (self.num == num):
            self.health -= damage
            print("the attack was very strong!")
        elif ((self.num - num == 1) or (self.num - num == -1)): # if the numbers are within 1 of eachother, 1/2 damage is dealt
            self.health -= damage / 2
            print("the attack was strong")
        elif ((self.num - num == 2) or (self.num - num == -2)): # if the numbers are within 2 of eachother, 1/4 damage is dealt
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
        elif (self.power == "cookie"):
            if uses > 0:
                self.health += 3
                print(self.name +"'s health:", self.health)
                print(self.power +" uses left: ",(uses - 1))
            else:
                print(self.power + " has been used up")
        elif (self.power == "sword"):
            if uses > 0:
                self.strength += 5
                print(self.name +"'s strength:", self.strength)
                print(self.power +" uses left: ",(uses - 1))
            else:
                print(self.power + " has already been equipped")
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
        if (self.num == num):
            self.health -= damage
            print("the attack was very strong!")
        elif ((self.num - num == 1) or (self.num - num == -1)):
            self.health -= damage / 2
            print("the attack was strong")
        elif ((self.num - num == 2) or (self.num - num == 2)):
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

# sets the player's name
name = input("what is your name? \n")
p1 = player(name, 5, 10, random.randint(1,4),0, None)

# tutorial/rules
print ("hello,",p1.name)
print("Type 'attack' to attack. Type 'quit' to quit the game.")

enemy_names = ["cave", "forest", "tree", "water", "fire"]
e1 = enemy("small " + enemy_names[(random.randint(0,4))] + " monster", 3, 5, (random.randint(1,4)), 3, 1)
e2 = enemy(enemy_names[(random.randint(0,4))] + " monster", 5, 5, (random.randint(1,4)), 9, 3)
e3 = enemy(enemy_names[(random.randint(0,4))] + " monster", 5, 10, (random.randint(1,4)), 15, 5)
boss = enemy("big "+ enemy_names[(random.randint(0,4))] + " monster", 8, 15, (random.randint(1,4)), 50, 10) 
strength_potion = item("strength potion", 15, 3, "increases strength by 5. Can be used 3 times.")
health_potion = item("health potion", 20, 5, "increases health by 5. Can be used 5 times.")
cookie = item("cookie", 2, 1, "increases health by 3. Can be used once.")
sword = item("sword", 8, 1, "increases strength by 5. Can be used once.")
 
battling = True

# function used for all battles 
def battle(e, power):
    p1.health = 10
    while (battling == True):
        print(" ")
        p1.take_damage(e1.attack(), e.strength, e.name)
        p1.check_health()
        
        # player loses
        if ((p1.health <= 0)):
            battling == False
            break

        ans = input("What do you do? \n")
        if (ans == p1.power):
            p1.use_power(power.uses)
            power.uses -= 1
        elif (ans == "attack"):
            e.take_damage(p1.attack(), (p1.strength), p1.name)
            e.check_health()
        elif (ans == "quit"):
            print("thanks for playing!")
            quit()
        else:
            print("invalid response! your turn has been skipped.")
    
        time.sleep(1.5)

        # player wins
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
# sets up the shop
shop_items = [strength_potion, health_potion, cookie, sword]
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
# the powerup that the player purchanced is used as a parameter in the battle function
if p1.power == strength_potion.name:
    battle(boss, strength_potion)
elif p1.power == health_potion.name:
    battle(boss, health_potion)
elif p1.power == cookie.name:
    battle(boss, cookie)
elif p1.power == sword.name:
    battle(boss, sword)
else:
    battle(boss, None)