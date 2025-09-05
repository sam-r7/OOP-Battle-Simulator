import random
class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    def __init__(self, name, health, atk, special_ability):
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

