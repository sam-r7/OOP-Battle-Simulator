from enemy import Enemy
import random

class Orc(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 400
        self.attack_power = 45

    def attack(self):
        mult = 1
        if random.randint(0, 10) == 1:
            print("CRITICAL STRIKE")
            mult = 3
            return random.randint(self.attack_power-30, self.attack_power-20) * mult
        else:
            return random.randint(self.attack_power-20, self.attack_power)
        
    def take_damage(self, damage):
        armor = int(0.15*damage)
        damage -= armor
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name}'s armor absorbs {armor}, and takes {damage} damage. Health is now {self.health}.")


        


