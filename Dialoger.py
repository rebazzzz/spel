import time


def pop_up_text(text, delay=1):
    words = text.split()
    for word in words:
        print(word, end=' ', flush=True)
        time.sleep(delay)

#dialoge3 = "är du här för Sten Jättens kärna vist ?"
#pop_up_text(dialoge3, delay=0.5)


# Title 

print (""" 
 __ _                        ___           _   _         
/ _\ |_ ___  _ __   ___     /   \___ _ __ | |_| |__  ___ 
\ \| __/ _ \| '_ \ / _ \   / /\ / _ \ '_ \| __| '_ \/ __|
_\ \ || (_) | | | |  __/  / /_//  __/ |_) | |_| | | \__ 
\__/\__\___/|_| |_|\___| /___,' \___| .__/ \__|_| |_|___/
                                    |_|                  
        """)

# Gamla Gubben

print (". . . länge sen jag har sett en person här")
time.sleep(2)

print ("ah berom hur sekt mitt namn är Gunnar.")
time.sleep(2)

print (" Du är väl här för Sten Jättens kärna vist ?")
time.sleep(2)

print ("Om du vill så kan jag ge dig lite information du kanske vill veta…")
time.sleep(2)

print ("Men ! Besvara min gåta och du får veta.")
time.sleep(2)
 
print ("Vad är stort och lysser stark i himlen")
time.sleep(2)

while True:
    svar = (input("skriv ditt svar:/n"))

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

# Boss

print ("""    00
             0000
             0000
              00
            .-''-.
           /  __  1
          /.-'  '-.1
          \::.  .::/
           \'    '/
      __ ___)    (___ __
    .'   \\        //   `.
   /     | '-.__.-' |     1
   |     |  '::::'  |     |
   |    /    '::'    \    |
   |_.-;\     __     /;-._|
   \.'^`\\    \/    //`^'./
   /   _.-._ _||_ _.-._   1
  `\___\    '-..-'    /___/`
       /'---.  `\.---'1
      ||    |`\\\|    ||
      ||    | || |    ||
      |;.__.' || '.__.;|
      |       ||       |
      11111111||11111111
       |      ||      |
       |.-==-.||.-==-.|
       <.    .||.    .>
        \'=='/||\'=='/
        |   / || \   |
        |   | || |   |
        |   | || |   |
        /^^\| || |/^^1
       /   .' || '.   1
      /   /   ||   \   1
     (__.'    \/    '.__)""")

#start upp sound
print ("Bzzzzzz")

print ("plin plin plon")

# Boss tar damage
print ("Crash!")

# Enemys

print ("raslande ben hörs kommande")

#Enemy dör
print ("plink plonk hör när skeletet faller ihop")

#Miljö beskrivning

#Room1
print ("Du stiger in grottan och känner av de kalla luften forsa över")

print ("Vid gråttans slut finns de två vägare en öppen gråt tunnel åt höger och en dörr åt vänser ")

print ("Du går mot dörren och försöker öppna den men den är låst och du går tillbaka till var du börja")

print ("du går igenom tunneln och kommer till ett nytt rum")

#om man har nyckeln 
print ("låst dörren öppnades och du går igenom")

#Room2

print ("Två öppna väggar är framför dig")

print ("Du går igenom tunneln rakt fram")

print ("Du går igenom tunneln åt höger")

#Deadend1

print ("du kommer fram till ett room med inga mer väggar men en kista är framför dig")

val = int(input("Vill du öppna kistan eller inte? (skriv 1 för att öppna, 2 för att inte)"))

if val == 1:
    print ("Du öppna kistan och hittade en flaska av liv som ger 50 hp")

if val == 2:
    print ("Du lämnade rummet och kom tillbaka till rummet du va innan i")

#Enemy room 1 

print ("Rummet är kallt och du har raslande ljud åt andra sidan grått rummet")

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
                 _.//7'                      | |
               '---'                         j_| `
                                            (| |
                                             |  1
                                             |lllj
                                             |||||  """)

print ("ett skelet kom fram!")

print ("raslande benen faller och en nyckel ligger på marken")

print ("Du har nu nyckel i din inventory.")

#Enemy room 2

print ("rummet känns kallare än för ut och ljud av fallande stenar hörs")

print ("något börjar komma fram från de mörka gråtta mot dig")

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

print("Skeletet har dött och du går till slutet av gråt rummet")

print ("Framför dig finns två dörrar en åt höger och en åt vänster")

#höger dörren

print("")