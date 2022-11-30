import random
#import player
#import enemy

class player:
    def __init__(self, name, strength, health, num):
        self.name = name
        self.strength = strength
        self.health = health
        self.num = num
    def take_damage(self, num, damage):
        print("the enemy attacked!")
        if (num == self.num):
            self.health -= damage
            print("the attack was strong!")
        elif (self.num - num == 1):
            self.health -= damage / 2
            print("the attack was weak")
        elif (self.num - num == 2):
            self.health -= damage / 4
            print("the attack was very weak")
        else:
            print("the attack failed!")
    def check_health(self):
        if (self.health <= 0):
            print("you lost!")
        else:
            print("Your health is: ", self.health)
    def heal(self):
        self.health += 3

class enemy:
    def __init__(self, strength, health, num):
        self.strength = strength
        self.health = health
        self.num = num
    def take_damage(self, num, damage, name):
        print(name, " attacked!")
        if (num == self.num):
            self.health -= damage
            print("the attack was strong!")
        elif (self.num - num == 1):
            self.health -= damage / 2
            print("the attack was weak")
        elif (self.num - num == 2):
            self.health -= damage / 4
            print("the attack was very weak")
        else:
            print("the attack failed!")

    def check_health(self):
        if (self.health <= 0):
            print("the enemy lost!")
        else:
            print("enemy's health is: ", self.health)
    def attack(self):
        return random.randint(0,5)


name = input("what is your name? \n")
p1 = player(name, 5, 10, random.randint(0,5))
print ("hello,",p1.name)

e1 = enemy(8, 10, (random.randint(0,5))) 

battle = True

while (battle == True):
    p1.take_damage(e1.attack(), e1.strength)
    p1.check_health()
    
    if ((p1.health <= 0)):
        battle == False
        break

    ans = input("What do you do? \n")
    if (ans == "heal"):
        p1.heal()
        p1.check_health()
    elif (ans == "attack"):
        attack = input("input a number between 0-5 \n")
        e1.take_damage(int(attack), (p1.strength), p1.name)
        e1.check_health()
    else:
        print("invalid response! your turn has been skipped.")
   
    if ((e1.health <= 0)):
        battle == False
        break
