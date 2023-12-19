import random

enemy_hp = 80
player_hp = 100
sword1 = 20
sword2 = 25
sword3 = 30

def spelare_attack():
    """Spelaren attackerar enemy genom att välja vapen"""
    global enemy_hp
    attack = int(input("Vilket vapen vill du använda Svärd1, svärd2 eller svärd3? Skriv 1, 2 eller 3 \n"))

    if attack == 1:
        enemy_hp -= sword1
        if enemy_hp < 0:
            print(f"Enemy har nu 0 hp efter din attack.")
        else:
            print(f"Enemy har nu {enemy_hp} hp efter din attack.")
    elif attack == 2:
        enemy_hp -= sword2 
        if enemy_hp < 0:
            print(f"Enemy har nu 0 hp efter din attack.")
        else:
            print(f"Enemy har nu {enemy_hp} hp efter din attack.")
    elif attack == 3:
        enemy_hp -= sword3
        if enemy_hp < 0:
            print(f"Enemy har nu 0 hp efter din attack.")
        else:
            print(f"Enemy har nu {enemy_hp} hp efter din attack.")
    else:
        print("Använd rätt vapen!")

def enemy_attack():
    """Enemy attackerar spelaren med random damage"""
    global player_hp
    damage = random.randint(10, 20)
    player_hp -= damage
    if player_hp < 0:
        print(f"Du har nu 0 hp efter enemy attack.")
    else:
        print(f"Du har nu {player_hp} hp efter enemy attack.")

while player_hp > 0 or enemy_hp > 0:
    spelare_attack()
    if enemy_hp <= 0:
        print("Enemy är död")
        break

    enemy_attack()
    if player_hp <= 0:
        print("GAME OVER")
        break