# globala variabler
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

# funktion för det som händer i rummen
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
        
        item_room = True
        item = True

    elif place == 2 and horizont == "right" and item_room == True:
        print("hej")

    elif place == 3 and horizont == "right" and enemy1_room == False:
        
        enemy1_room = True
        key1 = True
    
    elif place == 3 and horizont == "right" and enemy1_room == True:
        print("hej")
    
    elif place == 1 and horizont == "left" and enemy2_room == False:

        enemy2_room = True
    
    elif place == 1 and horizont == "left" and enemy2_room == True:
        print("hej")

    elif place == 2 and horizont == "left" and riddle_room == False:

        riddle_room = True
        key2 = True
    
    elif place == 2 and horizont == "left" and riddle_room == True:
        print("hej")
    
    elif place == 4 and wiseman_room == False:

        wiseman_room = True
    
    elif place == 4 and wiseman_room == True:
        print
    elif place == 6:
        death = True
    elif place == 7:
        win = True
        


# funktion för vart man kan gå om man kan gå överallt
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

        general_option = input("1 för vänster - 0 för höger  - 3 för backåt")

        if general_option == "0":
            place = place + 1
        elif general_option == "1":
            place = place + 1
        elif general_option == "3":
            place = place - 1
        else:
            print("du kan bara skriva 0 - 1 - 3")

# funktion för vart man går i början
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
    start_option = input("1 för vänster - 0 för höger")

    if start_option == "0":
        horizont = "right"
        place = place + 1
    elif start_option == "1":
        horizont = "left"
        place = place + 1

# funktion för vart man går om man bara kan gå backåt
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
        deadend_option = input("du kan bara gå backåt - 3 för backåt")
    
        if deadend_option == "3":
           place = place - 1
        else:
            print("du kan bara skriva 3")

# funktion för hela spelets movement och vart man kan gå beroende på vart man är
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
        
            start_option = input("1 för vänster (låst) - 0 för höger")

            if start_option == "0":
                horizont = "right"
                place = place + 1
            elif start_option == "1":
                print("dörren är låst, hitta nyckeln")
            else: 
                print("du kan bara skriva 1 eller 0")

    elif place == 1 and horizont == "right" and key1 == False:
        print("Hitta nyckeln")
        general_option = None
        while general_option not in ["0", "1", "3"]:

            general_option = input("1 för vänster - 0 för höger  - 3 för backåt")

            if general_option == "0":
                place = place + 1
            elif general_option == "1":
                place = place + 2
            elif general_option == "3":
                place = place - 1
                horizont = None
            else:
                print("du kan bara skriva 0 - 1 - 3")
            
    elif place == 2 and horizont == "right" and key1 == False:
        print("Hitta nyckeln")
        general_option = None
        while general_option not in ["0", "1", "3"]:

            general_option = input("1 för vänster - 0 för höger  - 3 för backåt")

            if general_option == "0":
                place = place + 1
            elif general_option == "1":
                place = place + 2
            elif general_option == "3":
                place = place - 1
            else:
                print("du kan bara skriva 0 - 1 - 3")
            
    elif place == 3 and horizont == "right" and key1 == False:
        print("Hitta nyckeln")
        deadend_option = None
        while deadend_option != "0":
            deadend_option = input("du kan bara gå backåt - 0 för backåt")
    
            if deadend_option == "0":
                place = place - 2
            else:
                print("du kan bara skriva 0")

    elif place == 1 and horizont == "right" and key1 == True:
        print("du har nyckeln, gå tillbaks och öppna dörren")
        general_option = None
        while general_option not in ["0", "1", "3"]:

            general_option = input("1 för vänster - 0 för höger  - 3 för backåt")

            if general_option == "0":
                place = place + 1
            elif general_option == "1":
                place = place + 2
            elif general_option == "3":
                place = place - 1
                horizont = None
            else:
                print("du kan bara skriva 0 - 1 - 3")

    elif place == 2 and horizont == "right" and key1 == True:
        print("Det finns inget mer här")
        print("du har nyckeln, gå tillbaks till start")
        deadend()

    elif place == 3 and horizont == "right" and key1 == True:
        print("Det finns inget mer här")
        print("du har nyckeln, gå tillbaks till start")
        deadend_option = None
        while deadend_option != "0":
            deadend_option = input("du kan bara gå backåt - 0 för backåt")
    
            if deadend_option == "0":
                place = place - 2
            else:
                print("du kan bara skriva 0")

    elif place == 0 and horizont == None and key1 == True:
        print("du kan öppna vänsta dörren nu")
        option = None
        while option not in ["0", "1"]:
            option = input("1 för vänster - 0 för höger")

            if option == "0":
                horizont = "right"
                place = place + 1
            elif option == "1":
                horizont = "left"
                place = place + 1

    elif place == 1 and horizont == "left" and key2 == False:
        key_option = None
        while key_option not in ["0", "1", "3"]:
        
            key_option = input("1 för vänster (låst) - 0 för höger - 3 för att gå backåt")

            if key_option == "0":
                place = place + 1
            elif key_option == "1":
                print("dörren är låst, hitta den nya nyckeln")
            elif key_option == "3":
                place = place - 1
                horizont = None
            else: 
                print("du kan bara skriva 1 eller 0")

    elif place == 2 and horizont == "left" and key2 == False:
        deadend()

    elif place == 2 and horizont == "left" and key2 == True:
        print("Det finns inget mer här")
        deadend()

    elif place == 1 and horizont == "left" and key2 == True:
        print("du kan öppna den vänstra dörren nu")
        key_option = None
        while key_option not in ["0", "1", "3"]:
        
            key_option = input("1 för vänster - 0 för höger - 3 för att gå backåt")

            if key_option == "0":
                place = place + 1
            elif key_option == "1":
                place = place + 2
            elif key_option == "3":
                place = place - 1
                horizont = None
            else: 
                print("du kan bara skriva 1 eller 0")

    elif place == 3 and horizont == "left":
        key2_option = None
        while key2_option not in ["0", "1", "3"]:
        
            key2_option = input("1 för vänster - 0 för höger - 3 för att gå backåt")

            if key2_option == "0":
                place = place + 2
            elif key2_option == "1":
                place = place + 1
            elif key2_option == "3":
                place = place - 2
            else: 
                print("du kan bara skriva 1 eller 0")

    elif place == 4:
        deadend()

    elif place == 5:
        end_option = None
        while end_option not in ["0", "1", "3"]:
        
            end_option = input("1 för vänster - 0 för höger - 3 för att gå backåt")

            if end_option == "0":
                place = place + 1
            elif end_option == "1":
                place = place + 2
            elif end_option == "3":
                place = place - 2
            else: 
                print("du kan bara skriva 1 eller 0")
    elif place == 6:
        print("du dog")

    elif place == 7:
        print("du van")

# loop för hur positionen och evented körs i en loop tills man vinner eller förlorar
while win != True and death != True:
    position()
    event()
    print(place)

print("end")