import random, time

enemy_hp = 100
player_hp = 120

pickaxe = 25
yxa = 30
magisktlubba = 35
arsenal = ["Pickaxe 🪓", "Yxa 🔨", "Magisktlubba 🍭✨"]


def spelare_attack():
    """Spelaren attackerar enemy genom att välja vapen i sin arsenal"""
    global enemy_hp    
    attack = int(input("Skriv 1 för Pickaxe, 2 för xan och 3 för den magiska klubban:\n"))

    if attack == 1:
        enemy_hp -= pickaxe
        if enemy_hp < 0:
            print(f"Enemy har nu 0 hp efter din attack.")
        else:
            print(f"🦴💥: Enemy har nu {enemy_hp} hp efter din attack.")
    elif attack == 2:
        enemy_hp -= yxa
        if enemy_hp < 0:
            print(f"Enemy har nu 0 hp efter din attack.")
        else:
            print(f"🦴💥💥: Enemy har nu {enemy_hp} hp efter din attack.")
    elif attack == 3:
        enemy_hp -= magisktlubba
        if enemy_hp < 0:
            print(f"Enemy har nu 0 hp efter din attack.")
        else:
            print(f"🦴💥💥💥: Enemy har nu {enemy_hp} hp efter din attack.")
            #⚔️🦴💥
    else:
        print("Använd rätt vapen!")

def enemy_attack():
    """Enemy attackerar spelaren med random damage"""
    global player_hp
    damage = random.randint(20, 30)
    player_hp -= damage
    if player_hp < 0:
        print(f"Du har nu 0 hp efter enemy attack.")
    else:
        print(f"💥💥💥: Du har nu {player_hp} hp efter enemy attack.")

print (f"Du har dessa vapen i din arsenal: {arsenal}.")
time.sleep(2)

print(f"Din pickaxe gör 25 damage, yxan gör 30 och den magiska klubban gör 35!")
time.sleep(2)

print(f"Vilket vapen vill du attackera skeletten med?")
time.sleep(2)

while player_hp > 0 or enemy_hp > 0:
    spelare_attack()
    time.sleep(0.5)
    if enemy_hp <= 0:
        print("Enemy är död")
        break

    enemy_attack()
    time.sleep(0.5)
    if player_hp <= 0:
        print("GAME OVER")
        break