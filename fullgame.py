import Dialoger, time, skelet, lavaskelet, boss

place = 0
horizont = None
key1 = False
key2 = False
item_room = False
item = False
wiseman_room = False
enemy1_room = False
enemy2_room = False
riddle_room = False

death = False
win = False

def event():
    global place
    global horizont
    global key1
    global key2
    global item_room
    global item
    global wiseman_room
    global enemy1_room
    global enemy2_room
    global riddle_room
    global death
    global win
    if place == 2 and horizont == "right" and item_room == False:
        Dialoger.deadend1()
        item_room = True
        item = True

    elif place == 2 and horizont == "right" and item_room == True:
        print("Hej")

    elif place == 3 and horizont == "right" and enemy1_room == False:
        Dialoger.enemyroom1()
        skelet.combat_guide()
        skelet.skelet_combatloop()
        enemy1_room = True
        key1 = True
    
    elif place == 3 and horizont == "right" and enemy1_room == True:
        print("Hej")
    
    elif place == 1 and horizont == "left" and enemy2_room == False:
        Dialoger.enemyroom2()
        lavaskelet.combat_guide()
        lavaskelet.lavaskelet_combatloop()
        enemy2_room = True
    
    elif place == 1 and horizont == "left" and enemy2_room == True:
        print("Hej")

    elif place == 2 and horizont == "left" and riddle_room == False:
        Dialoger.riddle()
        riddle_room = True
        key2 = True
    
    elif place == 2 and horizont == "left" and riddle_room == True:
        print("Hej")
    
    elif place == 4 and wiseman_room == False:
        Dialoger.oldman()
        wiseman_room = True
    
    elif place == 4 and wiseman_room == True:
        print

    elif place == 5:
        Dialoger.boss()
        boss.combat_guide()
        boss.boss_combatloop()
        Dialoger.bossdead()

    elif place == 6:
        Dialoger.lastright()
        death = True

    elif place == 7:
        Dialoger.lastleft()
        win = True
        



def movement():
    global place
    global horizont
    global key1
    global key2
    global item_room
    global item
    global wiseman_room
    global enemy1_room
    global enemy2_room
    global riddle_room
    global death
    global win
    general_option = None
    while general_option not in ["0", "1", "3"]:

        general_option = input("Vart vill du gå? (Ange 1 för vänster, 0 för höger eller 3 för att gå backåt):\n")

        if general_option == "0":
            place = place + 1
        elif general_option == "1":
            place = place + 1
        elif general_option == "3":
            place = place - 1
        else:
            print("Du kan bara skriva 0, 1 eller 3 !!!")

def start_movement():
    global place
    global horizont
    global key1
    global key2
    global item_room
    global item
    global wiseman_room
    global enemy1_room
    global enemy2_room
    global riddle_room
    global death
    global win
    start_option = input("Vill du gå vänster eller höger? (Ange 1 för vänster eller 0 för höger):\n")

    if start_option == "0":
        horizont = "right"
        place = place + 1
    elif start_option == "1":
        horizont = "left"
        place = place + 1

    
def deadend():
    global place
    global horizont
    global key1
    global key2
    global item_room
    global item
    global wiseman_room
    global enemy1_room
    global enemy2_room
    global riddle_room
    global death
    global win
    deadend_option = None
    while deadend_option != "3":
        deadend_option = input("Du kan bara gå bak just nu!!! (Ange 3 för att gå backåt):\n")
    
        if deadend_option == "3":
           place = place - 1
        else:
            print("Du kan bara skriva 3 !!!")

def position():
    global place
    global horizont
    global key1
    global key2
    global item_room
    global item
    global wiseman_room
    global enemy1_room
    global enemy2_room
    global riddle_room
    global death
    global win
    if place == 0 and horizont == None and key1 == False:
        
        start_option = None
        while start_option not in ["0", "1"]:
        
            start_option = input("Vill du gå vänster eller höger? (Ange 1 för vänster eller 0 för höger):\n")

            if start_option == "0":
                Dialoger.caveright()
                horizont = "right"
                place = place + 1
            elif start_option == "1":
                Dialoger.caveleft()
            else: 
                print("Du kan bara skriva 1 eller 0 !!!")

    elif place == 1 and horizont == "right" and key1 == False:
        Dialoger.room2()
        print("Du behöver att hitta en nyckel!")
        general_option = None
        while general_option not in ["0", "1", "3"]:

            general_option = input("Vart vill du gå? (Ange 1 för vänster, 0 för höger eller 3 för att gå backåt):\n")

            if general_option == "0":
                Dialoger.rightdoor1()
                place = place + 1
            elif general_option == "1":
                Dialoger.leftdoor1()
                place = place + 2
            elif general_option == "3":
                place = place - 1
                horizont = None
            else:
                print("Du kan bara skriva 0, 1 eller 3 !!!")
            
    elif place == 2 and horizont == "right" and key1 == False:
        Dialoger
        print("Du behöver att hitta en nyckel!")
        general_option = None
        while general_option not in ["0", "1", "3"]:

            general_option = input("Vart vill du gå nu? (Ange 1 för vänster, 0 för höger eller 3 för att gå backåt):\n")

            if general_option == "0":
                place = place + 1
            elif general_option == "1":
                place = place + 2
            elif general_option == "3":
                place = place - 1
            else:
                print("Du kan bara skriva 0, 1 eller 3 !!!")
            
    elif place == 3 and horizont == "right" and key1 == False:
        print("Du behöver att hitta en nyckel!")
        deadend_option = None
        while deadend_option != "0":
            deadend_option = input("Ange 0 för att gå backåt:\n")
    
            if deadend_option == "0":
                place = place - 2
            else:
                print("Bakåt är den enda vägen!(Ange 0 för att gå bakåt)")

    elif place == 1 and horizont == "right" and key1 == True:
        Dialoger.room2()
        print("Du har nyckeln nu, gå tillbaks och öppna dörren.")
        general_option = None
        while general_option not in ["0", "1", "3"]:

            general_option = input("Vart vill du gå? (Ange 1 för vänster, 0 för höger eller 3 för att gå backåt):\n")

            if general_option == "0":
                Dialoger.rightdoor1()
                place = place + 1
            elif general_option == "1":
                Dialoger.leftdoor1()
                place = place + 2
            elif general_option == "3":
                place = place - 1
                horizont = None
            else:
                print("Du kan bara skriva 0, 1 eller 3 !!!")

    elif place == 2 and horizont == "right" and key1 == True:
        print("Det finns inget mer här")
        print("Du har nyckeln, gå tillbaks till start!")
        deadend()

    elif place == 3 and horizont == "right" and key1 == True:
        print("Det finns inget mer här.")
        print("Du har nyckeln, gå tillbaks till start.")
        deadend_option = None
        while deadend_option != "0":
            deadend_option = input("Du kan bara gå back just nu!!!(Ange 0 för att gå backåt):\n")
    
            if deadend_option == "0":
                place = place - 2
            else:
                print("Du kan bara skriva 0 !!!")

    elif place == 0 and horizont == None and key1 == True:
        print("Nu kan du öppna vänstra dörren!")
        option = None
        while option not in ["0", "1"]:
            option = input("Vill du gå höger eller vänster? (Ange 1 för vänster eller 0 för höger):\n")

            if option == "0":
                Dialoger.caveright()
                horizont = "right"
                place = place + 1
            elif option == "1":
                Dialoger.havekey()
                horizont = "left"
                place = place + 1

    elif place == 1 and horizont == "left" and key2 == False:
        key_option = None
        while key_option not in ["0", "1", "3"]:
        
            key_option = input("Vart vill du gå? (Ange 1 för vänster, 0 för höger eller 3 för att gå backåt):\n")

            if key_option == "0":
                place = place + 1
            elif key_option == "1":
                print("Dörren är låst, du behöver hitta den nya nyckeln!")
            elif key_option == "3":
                place = place - 1
                horizont = None
            else: 
                print("Du kan bara skriva 1 eller 0 !!!")

    elif place == 2 and horizont == "left" and key2 == False:

        deadend()

    elif place == 2 and horizont == "left" and key2 == True:
        print("Det finns inget mer här.")
        deadend()

    elif place == 1 and horizont == "left" and key2 == True:
        print("Nu kan du öppna den vänstra dörren!")
        key_option = None
        while key_option not in ["0", "1", "3"]:
        
            key_option = input("Vart vill du gå? (Ange 1 för vänster, 0 för höger eller 3 för att gå backåt):\n")

            if key_option == "0":
                place = place + 1
            elif key_option == "1":
                Dialoger.nyckelnvänster()
                Dialoger.emptyroom()
                place = place + 2
            elif key_option == "3":
                place = place - 1
                horizont = None
            else: 
                print("Du kan bara skriva 1 eller 0 !!!")

    elif place == 3 and horizont == "left":
        key2_option = None
        while key2_option not in ["0", "1", "3"]:
        
            key2_option = input("Vart vill du gå? (Ange 1 för vänster, 0 för höger eller 3 för att gå backåt):\n")

            if key2_option == "0":
                place = place + 2
            elif key2_option == "1":
                place = place + 1
            elif key2_option == "3":
                place = place - 2
            else: 
                print("Du kan bara skriva 1 eller 0 !!!")

    elif place == 4:
        deadend()

    elif place == 5:
        end_option = None
        while end_option not in ["0", "1", "3"]:
        
            end_option = input("Vart vill du gå? (Ange 1 för vänster, 0 för höger eller 3 för att gå backåt):\n")

            if end_option == "0":
                place = place + 1
            elif end_option == "1":
                place = place + 2
            elif end_option == "3":
                place = place - 2
            else: 
                print("Du kan bara skriva 1 eller 0 !!!")
    elif place == 6:
        print("DU DOG")

    elif place == 7:
        print("DU VANN")

Dialoger.title()
Dialoger.room1()

def stone_depth():
    global death
    global win
    while win != True and death != True:
        position()
        event()
    
    print("The End")

