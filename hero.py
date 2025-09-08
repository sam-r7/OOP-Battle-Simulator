import random
class Hero:

    def __init__(self, name, health, atk):
        self.name = name
        self.health = health
        self.atk = atk
    

    def strike(self):
        return random.randint((self.atk-15), (self.atk+15))
    
    def fireball(self):
        return random.randint(90, 120)
    
    def receive_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(self.name + " takes " + str(damage) + " damage. Health is now " + str(self.health))
    
    def is_alive(self):
        return self.health > 0

