import random
import os

# discarded
# discarded
# discarded
# discarded
# THIS HAS MANY BUGG PLEASE DO NOT USE IT IN THE SCRIPT.

b1="""

 /$$      /$$            /$$$$$$       /$$$$$$  /$$                 /$$ /$$
| $$$    /$$$           /$$__  $$     /$$__  $$| $$                | $$| $$
| $$$$  /$$$$  /$$$$$$$| $$  \__/    | $$  \__/| $$$$$$$   /$$$$$$ | $$| $$
| $$ $$/$$ $$ /$$_____/| $$$$ /$$$$$$|  $$$$$$ | $$__  $$ /$$__  $$| $$| $$
| $$  $$$| $$|  $$$$$$ | $$_/|______/ \____  $$| $$  \ $$| $$$$$$$$| $$| $$
| $$\  $ | $$ \____  $$| $$           /$$  \ $$| $$  | $$| $$_____/| $$| $$
| $$ \/  | $$ /$$$$$$$/| $$          |  $$$$$$/| $$  | $$|  $$$$$$$| $$| $$
|__/     |__/|_______/ |__/           \______/ |__/  |__/ \_______/|__/|__/
                                                                           
Use the help command if you want help!

"""

b2="""

 ███▄ ▄███▓  ██████   █████▒ ██████  ██░ ██ ▓█████  ██▓     ██▓    
▓██▒▀█▀ ██▒▒██    ▒ ▓██   ▒▒██    ▒ ▓██░ ██▒▓█   ▀ ▓██▒    ▓██▒    
▓██    ▓██░░ ▓██▄   ▒████ ░░ ▓██▄   ▒██▀▀██░▒███   ▒██░    ▒██░    
▒██    ▒██   ▒   ██▒░▓█▒  ░  ▒   ██▒░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██░    
▒██▒   ░██▒▒██████▒▒░▒█░   ▒██████▒▒░▓█▒░██▓░▒████▒░██████▒░██████▒
░ ▒░   ░  ░▒ ▒▓▒ ▒ ░ ▒ ░   ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░
░  ░      ░░ ░▒  ░ ░ ░     ░ ░▒  ░ ░ ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░ ░ ▒  ░
░      ░   ░  ░  ░   ░ ░   ░  ░  ░   ░  ░░ ░   ░     ░ ░     ░ ░   
       ░         ░               ░   ░  ░  ░   ░  ░    ░  ░    ░  ░
                                                                   
Remember that there are updates!, use the update command

"""

b3="""



███╗   ███╗███████╗███████╗    ███████╗██╗  ██╗███████╗██╗     ██╗     
████╗ ████║██╔════╝██╔════╝    ██╔════╝██║  ██║██╔════╝██║     ██║     
██╔████╔██║███████╗█████╗█████╗███████╗███████║█████╗  ██║     ██║     
██║╚██╔╝██║╚════██║██╔══╝╚════╝╚════██║██╔══██║██╔══╝  ██║     ██║     
██║ ╚═╝ ██║███████║██║         ███████║██║  ██║███████╗███████╗███████╗
╚═╝     ╚═╝╚══════╝╚═╝         ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝

LLLLLL IIIIIII KKKKKKK EEEEEEE  https://github.com/GeerxOS/msf-shell                                                                  

"""

b4="""

 /'\_/`\          /'___\ 
/\      \    ____/\ \__/ 
\ \ \__\ \  /',__\ \ ,__|
 \ \ \_/\ \/\__, `\ \ \_/                 
  \ \_\\ \_\/\____/\ \_\ 
   \/_/ \/_/\/___/  \/_/ 
                         
                                            +------------------------------------------------+
                                            |      Commands                                  |
                                            | Command          | Description                 |  
                                            | use              | Use a payload or auxiliary. |
                                            | help             | Show available commands.    |
                                            | exit             | Finish the script.          |
                                            | update           | Update the script           |
                                            | show credits     | Show the credits.           |
                                            | banner           | Show the banner.            |
                                            | show payloads    | Show Payloads.              |
                                            | show beta        | Show beta options.          |
                                            | show auxiliarys  | Show Auxiliarys.            |
                                            | show exploits    | Show Exploits.              |
                                            | add              | Add the tool to the terminal|
                                            +------------------------------------------------+

 ____    __              ___    ___      
/\  _`\ /\ \            /\_ \  /\_ \     
\ \,\L\_\ \ \___      __\//\ \ \//\ \    
 \/_\__ \\ \  _ `\  /'__`\\ \ \  \ \ \   
   /\ \L\ \ \ \ \ \/\  __/ \_\ \_ \_\ \_ 
   \ `\____\ \_\ \_\ \____\/\____\/\____|
    \/_____/\/_/\/_/\/____/\/____/\/____/
                                         
Exploit! Exploit! Payload! Payload! Looks vulnerable! ("hack!")         

"""

b5="""



  o          o                o__ __o                o__ __o      o                        o    o  
 <|\        /|>              /v     v\              /v     v\    <|>                      <|>  <|> 
 / \\o    o// \             />       <\            />       <\   / >                      / \  / \ 
 \o/ v\  /v \o/      __o__  \o                    _\o____        \o__ __o      o__  __o   \o/  \o/ 
  |   <\/>   |      />  \    |>_         _\__o__       \_\__o__   |     v\    /v      |>   |    |  
 / \        / \     \o       |                \              \   / \     <\  />      //   / \  / \ 
 \o/        \o/      v\     <o>                    \         /   \o/     o/  \o    o/     \o/  \o/ 
  |          |        <\     |                      o       o     |     <|    v\  /v __o   |    |  
 / \        / \  _\o__</    / \                     <\__ __/>    / \    / \    <\/> __/>  / \  / \ 


Use the help command for help!!                                                                                              
                                                                                                   

"""

b6="""
                             .-.                              ___                 ___   ___  
                            /    \                           (   )               (   ) (   ) 
 ___ .-. .-.       .--.     | .`. ;                  .--.     | | .-.     .--.    | |   | |  
(   )   '   \    /  _  \    | |(___)               /  _  \    | |/   \   /    \   | |   | |  
 |  .-.  .-. ;  . .' `. ;   | |_       .------.   . .' `. ;   |  .-. .  |  .-. ;  | |   | |  
 | |  | |  | |  | '   | |  (   __)    (________)  | '   | |   | |  | |  |  | | |  | |   | |  
 | |  | |  | |  _\_`.(___)  | |                   _\_`.(___)  | |  | |  |  |/  |  | |   | |  
 | |  | |  | | (   ). '.    | |                  (   ). '.    | |  | |  |  ' _.'  | |   | |  
 | |  | |  | |  | |  `\ |   | |                   | |  `\ |   | |  | |  |  .'.-.  | |   | |  
 | |  | |  | |  ; '._,' '   | |                   ; '._,' '   | |  | |  '  `-' /  | |   | |  
(___)(___)(___)  '.___.'   (___)                   '.___.'   (___)(___)  `.__.'  (___) (___) 
                                                                                             
                                                                                            
h e l p c o m m a n d t a c o s ! ! !                                                                                           

"""

b7="""

+-----------------------|-----------------------|-----------------------+
|                                                                       |
|  #     #                      #####                                   |
|  ##   ##  ####  ######       #     # #    # ###### #      #           |
|  # # # # #      #            #       #    # #      #      #           |
|  #  #  #  ####  #####  #####  #####  ###### #####  #      #           |
|  #     #      # #                  # #    # #      #      #           |
|  #     # #    # #            #     # #    # #      #      #           |
|  #     #  ####  #             #####  #    # ###### ###### ######      |
|                                                                       |
+-----------------------|-----------------------|-----------------------+

"""
def baners():
    if random.randint(1, 7) == 1:
        print(b1)

    if random.randint(1, 7) == 2:
        print(b2)

    if random.randint(1, 7) == 3:
        print(b3)

    if random.randint(1, 7) == 4:
        print(b4)

    if random.randint(1, 7) == 5:
        print(b5)

    if random.randint(0, 7) == 6:
        print(b6)

    if random.randint(0, 7) == 0:
        print(b7)
    
    if random.randint(0, 7) == 0:
        print(b7)