class player:
    def __init__(self, name, strength, health):
        self.name = name
        self.strength = strength
        self.health = health
    def take_damage(self, damage):
        self.health -= damage
