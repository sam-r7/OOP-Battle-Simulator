from enemy import Enemy
import random

class Orc(Enemy):

    def __init__(self, name):
        super().__init__(name)
        self.health = 350
        self.attack_power = 45

    def attack(self):
        mult = 1
        if random.randint(0, 5) == 1:
            print("CRITICAL STRIKE")
            mult = 3
            return random.randint(self.attack_power-10, self.attack_power) * mult
        
    def take_damage(self, damage):
        armor = int(0.25*damage)
        damage -= armor
        self.health -= damage
        if self.health < 0:
            self.health == 0
        print(f"{self.name}'s armor absorbs {armor}, and takes {damage} damage. Health is now {self.health}.")
    
        

        


