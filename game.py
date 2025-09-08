import random
from goblin import Goblin
from hero import Hero
from orc import Orc

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Aragorn", 350, 50)
    cooldown = 1

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}") for i in range(3)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0

    stage = 1

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
        orc = Orc("Orc Boss")

    # Battle Loop 

        while hero.is_alive() and orc.is_alive():
            print("\nNew Round!")
            damage = hero.strike()
            orc.take_damage(damage)
            if orc.is_alive():
                damage = orc.attack()
                hero.receive_damage(damage)

            if cooldown == 0 and orc.is_alive():
                damage = hero.fireball()
                print(f"Hero casts fireball on "+ orc.name +" for " + str(damage) + " damage!")
                orc.take_damage(damage)
                cooldown = 3
            else:
                cooldown -= 1

    # Determine outcome
    if hero.is_alive():
        print(f"\nCongratulations, you defeated the boss!")
        print("You win!!! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")


if __name__ == "__main__":
    main()
