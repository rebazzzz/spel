import time


def pop_up_text(text, delay=1):
    words = text.split()
    for word in words:
        print(word, end=' ', flush=True)
        time.sleep(delay)




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
  print ("Du stiger in grottan och känner av de kalla luften forsa över")
  time.sleep(2)

  print ("Vid gråttans slut finns de två vägar en öppen gråt tunnel åt höger och en dörr åt vänser ")
  time.sleep(2)

def caveleft ():
  print ("Du går mot dörren och försöker öppna den men den är låst och du går tillbaka till var du börja")
  time.sleep(2)

def caveright():
  print ("Du går igenom tunneln och kommer till ett nytt rum")
  time.sleep(2)


#om man har nyckeln 
def havekey():
  print ("låsta dörren öppnades och du går igenom")

#Room2
def room2():
  print ("Två öppna vägar är framför dig en åt höger och en åt vänster")
  time.sleep(2)

def straightdoor():
  print ("Du går igenom tunneln rakt fram")
  time.sleep(2)

def rightdoor1():
  print ("Du går igenom tunneln åt höger")
  time.sleep(2)


#Deadend1
def deadend1():
  print ("Du kommer fram till ett room med inga mer väggar men en kista är framför dig")
  time.sleep(2)

  val = int(input("Vill du öppna kistan eller inte? (skriv 1 för att öppna, 2 för att inte)"))

  if val == 1:
     print ("Du öppna kistan och hittade inget där de bara stenar och kol inuti")

  if val == 2:
     print ("Du lämnade rummet och kom tillbaka till rummet du va innan i")

#Enemy room 1 
def enemyroom1():
 print ("Rummet är kallt och du hör raslande ljud åt andra sidan grått rummet")
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

 print ("Ett skelet kom fram!")

def DeadEnemy1():
 print ("Raslande benen faller och en nyckel ligger på marken")
 time.sleep(2)

 print ("Du har nu nyckel i din inventory.")
 time.sleep(2)


#Enemy room 2
def enemyroom2():
 print ("rummet känns kallare än för ut och ljud av fallande stenar hörs")
 time.sleep(2)

 print ("något börjar komma fram från de mörka gråtta mot dig")
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
 print("Skeletet har dött och du går till slutet av gråt rummet")
 time.sleep(2)

 print ("Framför dig finns två dörrar en åt höger och en åt vänster")
 time.sleep(2)

#höger dörren
def rightdoor2():
 print("Dörren är olåst och du går igenom den")

#vänster dörren
def leftdoor():
 print("Dörren är låst...")

#om man har nyckeln
def nyckelnvänster():
 print("de låsta dörren öppnades och du går igenom dörren till nästa rum")

#Rum med gåttan
def riddle():
 print("rummet är upplyst av lysande crystaler runt om i gråttan")
 time.sleep(2)

 print("du ser en liten staty av en drake i mitten av rummet")
 time.sleep(2)

 print("statyn börjar röra sig och dess ögon öppnas")
 time.sleep(2)

 punkt = (". . .")
 pop_up_text(punkt, delay=0.5)

 print("Mitt namn är Draku")
 time.sleep(2)

 print("besvara min gåtta rätt och jag ger dig nyckeln till de låsta dörren")
 time.sleep(2)

 dragonquest = input(". . . jag lysser upp natten och styr havets vågor men lysser inte lika starkt som solen vad är jag ?")
 while True:
   if dragonquest == "måne" or "månen":
     print("De rätt")
     break

   else:
     print("försök igen")

 print("du fick en nyckle till rummet")
 time.sleep(2)

#Tomt rum
def emptyroom():
 print("Du kliver in i the mörka rummet och tänder ett ljus")
 time.sleep(2)

 print("Du ser två öppna dörrar en åt väster och en åt höger")
 time.sleep(2)

#Gamla gubbens rum
def oldman():
 print("Du kliver in i de vänstra dörren och kollar runt")
 time.sleep(2)

 print("de hörs raslande ljud ...")
 time.sleep(2)

 print ("länge sen jag har sett en person här")
 time.sleep(2)

 print ("ah berom ursekt mitt namn är Gunnar.")
 time.sleep(2)

 print ("Du är väl här för Sten Jättens kärna vist ?")
 time.sleep(2)

 print ("Om du vill så kan jag ge dig lite information du kanske vill veta…")
 time.sleep(2)

 print ("Men ! Besvara min gåta och du får veta.")
 time.sleep(2)
 
 print ("Vad är stort och lysser stark i himlen")
 time.sleep(2)

 while True:
     svar = (input("skriv ditt svar:"))

     if svar == "sol" or "solen":
        print("En sol de är rätt")
        break

     else:
         print("De är fel försök igen.")

 print ("Nu när du har besvarat rätt så ska jag ge dig ledtråden…")
 time.sleep(2)

 print ("Vid slutet så kommer två dörrar att visas… En leder till din död men den andra")
 time.sleep(2)

 print ("tar dig ut från den här gamla grottan… ")
 time.sleep(2)

 print ("Den åt vänster är dödlig … så lycka till nu med att ta ner stenjätten.")
 time.sleep(2)


#Boss rummet.
def boss():
 print("du går igenom högra dörren och bemöts av en intense känsla")
 time.sleep(2)

 print("stenar och sand faller ner från vägarna")
 time.sleep(2)

 print("plin plin plon ...")
 time.sleep(2)

 print("tunga steg hörs kommande mot dig ...")
 time.sleep(2)

 print("kommandes från mörkret är stenjätten")
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
 print("stenar faller från stenjätten och dör")
 time.sleep(2)

 print("du plockar upp kärnan som du letade efter. ")
 time.sleep(2)

 print("bakom jättens kropp ser du två dörrar en åt höger och en åt vänster")
 time.sleep(2)


#vänster dörren
def lastleft():
 print("du öppnar dörren och kliver in")
 time.sleep(2)

 print("EN GIGANTISK STEN KULA KOMMER FALLANDES MOT DIG")
 time.sleep(2)

 print("du försöker springa i väg men blir krossad")
 time.sleep(2)

#höger dörren
def lastright():
 print("du öppnar dörren och kliver in")
 time.sleep(2)

 print("framför dig finns de trapor uppåt och du går upp dem")
 time.sleep(2)

 print("vid slutet av trapporna du öppnar en dörr och kommer ut från gråttan")
 time.sleep(2)

 print("Grattis du van!")
 time.sleep(2)