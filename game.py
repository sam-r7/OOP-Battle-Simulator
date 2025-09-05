import random
from goblin import Goblin
from hero import Hero
from orc import Orc

goblin_colors = ["blue", "red", "green", "orange"]

def main():
    stage = 1
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Aragorn", 325, 50)
    cooldown = 1

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}", (goblin_colors[random.randint(0, 3)])) for i in range(3)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0

    # Battle Loop 
    if stage == 1:
        while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
            print("\nNew Round!")
            
            # Hero's turn to attack
            target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
            damage = hero.strike()
            print(f"Hero attacks {target_goblin.name} for {damage} damage!")
            target_goblin.take_damage(damage)

            # Check if the target goblin was defeated
            if not target_goblin.is_alive():
                defeated_goblins += 1
                print(f"{target_goblin.name} has been defeated!")


            if cooldown == 0 and any(goblin.is_alive() for goblin in goblins):
                target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
                damage = hero.fireball()
                print(f"Hero casts fireball on {target_goblin.name} for {damage} damage!")
                target_goblin.take_damage(damage)
                cooldown = 3

                if not target_goblin.is_alive():
                    defeated_goblins += 1
                    print(f"{target_goblin.name} has been defeated!")

            else:
                cooldown -= 1

            # Goblins' turn to attack
            for goblin in goblins:
                if goblin.is_alive():
                    damage = goblin.attack()
                    print(f"{goblin.name} attacks hero for {damage} damage!")
                    hero.receive_damage(damage)

        # Determine outcome
        if hero.is_alive():
            print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
            stage = 2
        else:
            print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")


    if stage == 2:
        print("Boss approaches...")
        orc = [Orc("Orc Boss"), ]

    # Battle Loop 

        while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
            print("\nNew Round!")
            damage = hero.strike()
            orc.take_damage(damage)
            damage = orc.attack()
            hero.recieve_damage(damage)






if __name__ == "__main__":
    main()
