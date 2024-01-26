def map_guuide():
    print("""
          (Du är här) visar vart du är på kartan. Kartan är riktad mot dig, men pillarna visar vilken sida du kan gå.
          """)



def start_map():
    print("""
                                                         .:::::::::::::::::::::::.:....
                                                         .=                         ::.                        
                                                         .=       (Du är här)       ::.                        
:::::::::::::::::::::::...:::::::::::::::::::::::.:....  .=                         ::. 
=                     =. Höger:                                                     ::. 
=       DEAD END      =. ⬅️                   .=..........                         ::. 
=                                             .=        .= Höger:                  ::.  
=                     =. Vänster:⬇️           .=         .= ⬅️       Vänster:⬇️    ::.
=.....................=.:=.........    .........=        .=:::::::::::::::::::::    ::.                          
                         .---------    ----------                           .:::::  :::::::::::::::.  
                         :-                    .=                           ::.                   ::  
                         :-     SKELETT        .=                           ::.                   ::
                         :- (NYCKEL TILL       .=                           ::.  VÄNSTRA TUNNELN  ::
                         :- VÄNSTRA TUNNELN)   .=                           ::.                   ::
                         :-                    .=                           -...-:-::.:::::.:::...::               
                         :=.....:---==-=::.....:=           
                                                                     
          
          """)

def högra_tunneln_map():
    print("""   
                                                         .:::::::::::::::::::::::.:....
                                                         .=          START          ::.                        
                                                         .=                         ::.                        
:::::::::::::::::::::::...:::::::::::::::::::::::.:....  .=                         ::. 
=                     =. Höger:                                                     ::. 
=       DEAD END      =. ⬅️    (Du är här)     .=..........                         ::. 
=                                              .=        .= Höger:                  ::.  
=                     =. Vänster:⬇️           .=         .= ⬅️       Vänster:⬇️    ::.
=.....................=.:=.........    .........=        .=:::::::::::::::::::::    ::.                          
                         .---------    ----------                           .:::::  :::::::::::::::.  
                         :-                    .=                           ::.                   ::  
                         :-     SKELETT        .=                           ::.                   ::
                         :- (NYCKEL TILL       .=                           ::.  VÄNSTRA TUNNELN  ::
                         :- VÄNSTRA TUNNELN)   .=                           ::.                   ::
                         :-                    .=                           -...-:-::.:::::.:::...::               
                         :=.....:---==-=::.....:=           
                                                                     
          
          """)



def dead_end_map():
    print("""  
                                                         .:::::::::::::::::::::::.:....
                                                         .=          START          ::.                        
                                                         .=                         ::.                        
:::::::::::::::::::::::...:::::::::::::::::::::::.:....  .=                         ::. 
=                     =. Höger:                                                     ::. 
=     (Du är här)     =. ⬅️                    .=..........                         ::. 
=                                              .=        .= Höger:                  ::.  
=                     =. Vänster:⬇️           .=         .= ⬅️       Vänster:⬇️    ::.
=.....................=.:=.........    .........=        .=:::::::::::::::::::::    ::.                          
                         .---------    ----------                           .:::::  :::::::::::::::.  
                         :-                    .=                           ::.                   ::  
                         :-     SKELETT        .=                           ::.                   ::
                         :- (NYCKEL TILL       .=                           ::.  VÄNSTRA TUNNELN  ::
                         :- VÄNSTRA TUNNELN)   .=                           ::.                   ::
                         :-                    .=                           -...-:-::.:::::.:::...::               
                         :=.....:---==-=::.....:=           
                                                                     
          
          """)


def skelet_map():
    print("""  
                                                         .:::::::::::::::::::::::.:....
                                                         .=          START          ::.                        
                                                         .=                         ::.                        
:::::::::::::::::::::::...:::::::::::::::::::::::.:....  .=                         ::. 
=                     =. Höger:                                                     ::. 
=       DEAD END      =. ⬅️                    .=..........                         ::. 
=                                              .=        .= Höger:                  ::.  
=                     =. Vänster:⬇️           .=         .= ⬅️       Vänster:⬇️    ::.
=.....................=.:=.........    .........=        .=:::::::::::::::::::::    ::.                          
                         .---------    ----------                           .:::::  :::::::::::::::.  
                         :-                    .=                           ::.                   ::  
                         :-    (Du är här)     .=                           ::.                   ::
                         :-                    .=                           ::.  VÄNSTRA TUNNELN  ::
                         :-                    .=                           ::.                   ::
                         :-                    .=                           -...-:-::.:::::.:::...::               
                         :=.....:---==-=::.....:=           
                                                                     
          
          """)
    
def vänstra_tunneln_map():
    print("""
                                                         .:::::::::::::::::::::::.:....
                                                         .=          START          ::.                        
                                                         .=                         ::.                        
:::::::::::::::::::::::...:::::::::::::::::::::::.:....  .=                         ::. 
=                     =. Höger:                                                     ::. 
=       DEAD END      =. ⬅️                    .=..........                         ::. 
=                                              .=        .= Höger:                  ::.  
=                     =. Vänster:⬇️           .=         .= ⬅️       Vänster:⬇️    ::.
=.....................=.:=.........    .........=        .=:::::::::::::::::::::    ::.                          
                         .---------    ----------                           .:::::  :::::::::::::::.  
                         :-                    .=                           ::.                   ::  
                         :-     SKELETT        .=                           ::.                   ::
                         :- (NYCKEL TILL       .=                           ::.  (Du är här)      ::
                         :- VÄNSTRA TUNNELN)   .=                           ::.                   ::
                         :-                    .=                           -...-:-::.:::::.:::...::               
                         :=.....:---==-=::.....:=           
                                                                     
          
          """)


def lava_skelet_map():
    print("""
                                                         .:::::::::::::::::::::::.:....
                                                         .=       (Du är här)       ::.                        
                                                         .=                         ::.                        
                        ..:::::::::::::::::::::::.:....  .=                         ::. 
                      =.                                                            ::. 
                      =.        Draku          .=..........                         ::. 
                      =                        .=        .= Höger:                  ::.  
                      =.                       .=         .= ⬅️     Vänster:⬇️      ::.
                      .:=.......................=        .=:::::::::::::::::::::    ::.                          
                                                                            .:::::  :::::::::::::::.  
                                                                            ::.                   ::  
                                                                            ::.                   ::
                                                                            ::.   TOM TUNNEL      ::
                                                                            ::.                   ::
                                                                            -...-:-::.:::::.:::...::               
                                   
                                                               
          
          """)
    
def draku_map():
    print("""
                                                         .:::::::::::::::::::::::.:....
                                                         .=       LAVA SKELETT      ::.                        
                                                         .=                         ::.                        
                        ..:::::::::::::::::::::::.:....  .=                         ::. 
                      =.                                                            ::. 
                      =.        (Du är här)    .=..........                         ::. 
                      =                        .=        .= Höger:                  ::.  
                      =.                       .=         .= ⬅️     Vänster:⬇️      ::.
                      .:=.......................=        .=:::::::::::::::::::::    ::.                          
                                                                            .:::::  :::::::::::::::.  
                                                                            ::.                   ::  
                                                                            ::.                   ::
                                                                            ::.    TOM TUNNEL     ::
                                                                            ::.                   ::
                                                                            -...-:-::.:::::.:::...::               
                                   
                                                               
          
          """)
    
def tom_tunnel_map():
    print("""
                                                         .:::::::::::::::::::::::.:....
                                                         .=       LAVA SKELETT      ::.                        
                                                         .=                         ::.                        
                        ..:::::::::::::::::::::::.:....  .=                         ::. 
                      =.                                                            ::. 
                      =.        Draku          .=..........                         ::. 
                      =                        .=        .= Höger:                  ::.  
                      =.                       .=         .= ⬅️     Vänster:⬇️      ::.
                      .:=.......................=        .=:::::::::::::::::::::    ::.                          
                                                                            .:::::  :::::::::::::::.  
                                                                            ::.                   ::  
                                                                            ::.                   ::
                                                                            ::.  (Du är här nu)   ::
                                                                            ::.                   ::
                                                                            -...-:-::.:::::.:::...::               
                                   
                                                               
          
          """)



def tom_tunnel2_map():
    print("""
                                                         .:::::::::::::::::::::::.:....
                                                         .=       (Du är här)       ::.                        
                                                         .=                         ::.                        
                        ..:::::::::::::::::::::::.:....  .=                         ::. 
                      =.                                                            ::. 
                      =.       *******         .=..........                         ::. 
                      =                        .=        .= Höger:                  ::.  
                      =.                       .=         .= ⬅️     Vänster:⬇️      ::.
                      .:=.......................=        .=:::::::::::::::::::::    ::.                          
                                                                            .:::::  :::::::::::::::.  
                                                                            ::.                   ::  
                                                                            ::.    Gammal Man     ::
                                                                            ::.                   ::
                                                                            ::.                   ::
                                                                            -...-:-::.:::::.:::...::               
                                   
                                                               
          
          """)
    

def gammal_man_map():
    print("""
                                                         .:::::::::::::::::::::::.:....
                                                         .=       Tom Tunnel        ::.                        
                                                         .=                         ::.                        
                        ..:::::::::::::::::::::::.:....  .=                         ::. 
                      =.                                                            ::. 
                      =.       *******         .=..........                         ::. 
                      =                        .=        .= Höger:                  ::.  
                      =.                       .=         .= ⬅️     Vänster:⬇️      ::.
                      .:=.......................=        .=:::::::::::::::::::::    ::.                          
                                                                            .:::::  :::::::::::::::.  
                                                                            ::.                   ::  
                                                                            ::.   (Du är här)     ::
                                                                            ::.                   ::
                                                                            ::.                   ::
                                                                            -...-:-::.:::::.:::...::               
                                   
                                                               
          
          """)















def concept():
    print("""
                                                                        

:::::::::::::::::::::::. .:::::::::::=#*==-::::::.:. ..                             
=                     =. :-                    .+-=*:::-*:.                         
= .--.     :.:-.  ..  =..--:--...-....:-.      .=..........                        
= ::-=--==:=.:.:.+-:  =#@*-::+::-*:..:-:--=++=..=                                   
=                     =. :-   .::.             .=                               
=.....................=. :=.....................=                                     
........................ ...........*#-..........                        
                         .----------=*-----------                        
                         :-   :===-:::-==-=:   .=                        
                         :-  ..::..-.::::::.::..=                        
                         :-  +:===:-.:=-.:+-.-..=                        
                         :-  .. ...-..:.:.     .=                        
                         :=.....:---==-=::.....:=         


.:::::       :::::::::::.  
::.                    ::  
::.                    ::  
::.                    ::  
::.                    ::  
:-...-:-::.:::::.:::...::
      """)        