import time


def pop_up_text(text, delay=1):
    words = text.split()
    for word in words:
        print(word, end=' ', flush=True)
        time.sleep(delay)


# Jag har fått Asciiart från Asciiart.eu, Dessutom så fick jag time sleep samt delay text från en yt video.

# Title 
def title():
  print (""" 
  __ _                        ___           _   _         
 / _\ |_ ___  _ __   ___     /   \___ _ __ | |_| |__  ___ 
 \ \| __/ _ \| '_ \ / _ \   / /\ / _ \ '_ \| __| '_ \/ __|
 _\ \ || (_) | | | |  __/  / /_//  __/ |_) | |_| | | \__ 
 \__/\__\___/|_| |_|\___| /___,' \___| .__/ \__|_| |_|___/
                                    |_|                  
        """)

#Miljö beskrivning, Här börjar alla dialoger och text för varje rum.

#Room1

def room1():
  print ("Du stiger in grottan och känner av de kalla luften forsa över.\n")
  time.sleep(2)

  print ("Vid gråttans slut finns de två vägar en öppen gråt tunnel åt höger och en dörr åt vänser...\n")
  time.sleep(2)

def caveleft ():
  print ("Du går mot dörren och försöker öppna den men den är låst och du går tillbaka till var du börja.")
  time.sleep(2)

def caveright():
  print ("Du går igenom tunneln och kommer till ett nytt rum...")
  time.sleep(2)


#om man har nyckeln 
def havekey():
  print ("låsta dörren öppnades och du går igenom.")
  time.sleep(2)


#Room2
def room2():
  print ("Två öppna vägar är framför dig en åt höger och en åt vänster...")
  time.sleep(2)

def leftdoor1():
  print ("Du går igenom tunneln åt vänster!")
  time.sleep(2)

def rightdoor1():
  print ("Du går igenom tunneln åt höger!")
  time.sleep(2)


#Deadend1
def deadend1():
  print ("Du är inne i ett rum med inga mer vägar men en kista är framför dig!")
  time.sleep(2)

  val = int(input("Vill du öppna kistan eller inte? (skriv 1 för att öppna, 2 för att inte.):\n"))

  if val == 1:
     print ("Du öppna kistan och hittade inget där de bara stenar och kol inuti!")

  if val == 2:
     print ("Du valde att inte öppna kistan men du kan öppna den senare!")


#Enemy room 1 
def enemyroom1():
 print ("Rummet är kallt och du hör raslande ljud åt andra sidan grått rummet.")
 time.sleep(2)

 print("""
                               _.--""-._
   .                         ."         ".
  / \    ,^.         /(     Y             |      )1
 /   `---. |--'\    (  \__..'--   -   -- -'""-.-'  )
 |        :|    `>   '.     l_..-------.._l      .'
 |      __l;__ .'      "-.__.||_.-'v'-._||`"----"
  \  .-' | |  `              l._       _.'
   \/    | |                   l`^^'^^'j
         | |                _   \_____/     _
         j |               l `--__)-'(__.--' |
         | |               | /`---``-----'"1 |  ,-----.
         | |               )/  `--' '---'   \'-'  ___  `-.
         | |              //  `-'  '`----'  /  ,-'   I`.  1
       _ L |_            //  `-.-.'`-----' /  /  |   |  `. 1
      '._' / \         _/(   `/   )- ---' ;  /__.J   L.__.\ :
      `._;/7(-.......'  /        ) (     |  |            | |
       `._;l _'--------_/        )-'/     :  |___.    _._./ ;
         | |                 .__ )-'\  __  \  \  I   1   / /
         `-'                /   `-\-(-'   \ \  `.|   | ,' /
                            \__  `-'    __/  `-. `---'',-'
                               )-._.-- (        `-----'
                              )(  l\ o ('..-.
                        _..--' _'-' '--'.-. |
                 __,,-'' _,,-''            \ 1
                f'. _,,-'                   \ 1
               ()--  |                       \ 1
                 \.  |                       /  1
                   \ \                      |._  |
                    \ \                     |  ()|
                     \ \                     \  /
                      ) `-.                   | |
                     // .__)                  | |
                 _ ./ /7'                      | |
                '---'                         j_| `
                                             (| |
                                              |  1
                                              |lllj
                                              |||||  """)

 print ("Ett skelet kom fram!!!")

def DeadEnemy1():
 print ("Raslande benen faller och en nyckel ligger på marken...")
 time.sleep(2)

 print ("Du har nu nyckel i din inventory!")
 time.sleep(2)


#Enemy room 2
def enemyroom2():
 print ("Rummet känns kallare än för ut och ljud av fallande stenar hörs...")
 time.sleep(2)

 print ("Något börjar komma fram från de mörka gråtta mot dig!")
 time.sleep(2)

 print("""           )        )
                  (  (|              .
              )   )\/ ( ( (
      *  (   ((  /     ))\))  (  )    )
    (     \   )\(          |  ))( )  (|
    >)     ))/   |          )/  \((  ) 1
    (     (      .        -.     V )/   )(    (
     \   /     .   \            .       \))   ))
       )(      (  | |   )            .    (  /
      )(    ,'))     \ /          \( `.    )
      (\>  ,'/__      ))            __`.  /
     ( \   | /  ___   ( \/     ___   \ | ( (
      \.)  |/  /   \__      __/   \   \|  ))
     .  \. |>  \      | __ |      /   <|  /
          )/    \____/ :..: \____/     \ <
   )   \ (|__  .      / ;: \          __| )  (
  ((    )\)  ~--_     --  --      _--~    /  ))
   \    (    |  ||               ||  |   (  /
         \.  |  ||_             _||  |  /
           > :  |  ~V+-I_I_I-+V~  |  : (.
          (  \:  T\   _     _   /T  : ./
           \  :    T^T T-+-T T^T    ;<
            \..`_       -+-       _'  )
  )            . `--=.._____..=--'. ./     """)

 print("Ett skelet kom fram!!!")

def DeadEnemy2():
 print("Skeletet har dött och du går till slutet av gråt rummet.")
 time.sleep(2)

 print ("Framför dig finns två dörrar en åt höger och en åt vänster...")
 time.sleep(2)

#höger dörren
def rightdoor2():
 print("Dörren är olåst och du går igenom den.")

#vänster dörren
def leftdoor():
 print("Dörren är låst!")

#om man har nyckeln
def nyckelnvänster():
 print("De låsta dörren öppnades och du går igenom dörren till nästa rum...")

#Rum med gåttan
def riddle():
 print("Rummet är upplyst av lysande crystaler runt om i gråttan.")
 time.sleep(2)

 print("Du ser en liten staty av en drake i mitten av rummet...")
 time.sleep(2)

 print("Statyn börjar röra sig och dess ögon öppnas!!!")
 time.sleep(2)

 punkt = (". . .")
 pop_up_text(punkt, delay=0.5)

 print("Mitt namn är Draku.")
 time.sleep(2)

 print("Besvara min gåtta rätt och jag ger dig nyckeln till de låsta dörren.")
 time.sleep(2)

 dragonquest = input(". . . Jag lysser upp natten och styr havets vågor, men lysser inte lika starkt som min bror ?").lower()
 while True:
   if dragonquest == "måne" or "månen":
     print("Det är rätt!")
     break

   else:
     print("Gissa igen!")

 print("Du fick en nyckel till rummet!")
 time.sleep(2)

#Tomt rum
def emptyroom():
 print("Du kliver in i det mörka rummet och tänder ett ljus.")
 time.sleep(2)

 print("Du ser två öppna dörrar en åt vänster och en åt höger...")
 time.sleep(2)

#Gamla gubbens rum
def oldman():
 print("Du kliver in i de vänstra dörren och kollar runt...")
 time.sleep(2)

 print("De hörs raslande ljud!")
 time.sleep(2)

 print ("länge sen jag har sett en person här")
 time.sleep(2)

 print ("Ah! ber om ursäkt mitt namn är Gunnar.")
 time.sleep(2)

 print ("Du är väl här för Sten Jättens kärna vist?")
 time.sleep(2)

 print ("Om du vill så kan jag ge dig lite information du kanske vill veta…")
 time.sleep(2)

 print ("Men! Besvara min gåta och du får veta.")
 time.sleep(2)
 
 print ("Vad är stort och lysser stark i himlen?")
 time.sleep(2)

 while True:
     svar = (input("Vad gissar du på?")).lower()

     if svar == "sol" or "solen":
        print("Sol3n, det är rätt!")
        break

     else:
         print("Det är fel, försök igen!")

 print ("Nu när du har besvarat rätt så ska jag ge dig ledtråden…")
 time.sleep(2)

 print ("Vid slutet så kommer två dörrar att visas…")
 time.sleep(2)

 print ("Om du väljer dörren åt vänster så kommer glädje att falla över dig...")
 time.sleep(2)

#Boss rummet.
def boss():
 print("Du går igenom högra dörren och bemöts av en intensiv känsla...")
 time.sleep(2)

 print("Stenar och sand faller ner från vägarna!")
 time.sleep(2)

 print("PLIN PLIN PLON ...")
 time.sleep(2)

 print("Tunga steg hörs kommande mot dig...")
 time.sleep(2)

 print("kommandes från mörkret är stenjätten!")
 time.sleep(2)

 print("""                              ,--,  ,.-.
                ,                   \,       '-,-`,'-.' | ._
               /|           \    ,   |\         }  )/  / `-,',
               [ ,          |\  /|   | |        /  \|  |/`  ,`
               | |       ,.`  `,` `, | |  _,...(   (      .',
               \  \  __ ,-` `  ,  , `/ |,'      Y     (   /_L1
                \  \_\,``,   ` , ,  /  |         )         _,/
                 \  '  `  ,_ _`_,-,<._.<        /         /
                  ', `>.,`  `  `   ,., |_      |         /
                    \/`  `,   `   ,`  | /__,.-`    _,   `1
                -,-..\  _  \  `  /  ,  / `._) _,-\`       1
                 \_,,.) /\    ` /  / ) (-,, ``    ,        |
                ,` )  | \_\       '-`  |  `(               1
               /  /```(   , --, ,' \   |`<`    ,            |
              /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
        ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
       (-, \           ) \ ('_.-._)/ /,`    /
       | /  `          `/ \\ V   V, /`     /
    ,--\(        ,     <_/`\\     ||      /
   (   ,``-     \/|         \-A.A-`|     /
  ,>,_ )_,..(    )\          -,,_-`  _--`
 (_ \|`   _,/_  /  \_            ,--`
  \( `   <.,../`     `-.._   _,-`""")


#här i mellan så slås man mått jätten
def bossdead():
 print("Du plockar upp kärnan som du letade efter. ")
 time.sleep(2)

 print("Bakom jättens kropp ser du två dörrar en åt höger och en åt vänster...")
 time.sleep(2)


#vänster dörren
def lastleft():
 print("Du öppnar dörren och kliver in...")
 time.sleep(2)

 print("EN GIGANTISK STEN KULA KOMMER FALLANDES MOT DIG")
 time.sleep(2)

 print("Du försöker springa i väg men blir krossad!!!")
 time.sleep(2)

#höger dörren
def lastright():
 print("Du öppnar dörren och kliver in...")
 time.sleep(2)

 print("Framför dig finns de trapor uppåt och du går upp dem...")
 time.sleep(2)

 print("... vid slutet av trapporna öppnar du en dörr och kommer ut från gråttan!")
 time.sleep(2)

 print("Grattis du överlevde gråttan!!!")
 time.sleep(2)