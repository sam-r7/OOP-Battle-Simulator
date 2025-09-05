import random

class Enemy:
    def __init__(self, name):
        self.name = name
        self.health = random.randint(90, 120)
        self.attack_power = random.randint(7, 15)

    def attack(self):
        return random.randint(self.attack_power-20, self.attack_power)
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health == 0
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    def is_alive(self):
        return self.health > 0
        

    