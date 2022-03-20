import os
from sys import *

# Se importan los scripts

from colors import red, green, blue, yellow, purple, white

# Meterpreter

# Android Meterpreter

from meterpreter.android.and_http import and_http
from meterpreter.android.and_tcp import and_tcp

# Linux meterpreter

from meterpreter.linux.li_py import li_py
from meterpreter.linux.li64_http import li64_http
from meterpreter.linux.li64_tcp import li64_tcp
from meterpreter.linux.li86_http import li86_http
from meterpreter.linux.li86_tcp import li86_tcp

# Windows meterpreter

from meterpreter.windows.wind_http import wind_http
from meterpreter.windows.wind_py import wind_py
from meterpreter.windows.wind_tcp import wind_tcp

# Netcat

# Android NetCat
from netcat.android.and_net_http import and_net_http
from netcat.android.and_net_tcp import and_net_tcp

# Linux NetCat

from netcat.linux.li_net_py import li_net_py

# Windows NetCat

from netcat.windows.win_net_http import win_net_http
from netcat.windows.win_net_tcp import win_net_tcp
from netcat.windows.win_net_udp import win_net_udp

# Banners
help="""


 /'\_/`\          /'___\ 
/\      \    ____/\ \__/ 
\ \ \__\ \  /',__\ \ ,__|
 \ \ \_/\ \/\__, `\ \ \_/                 
  \ \_\\ \_\/\____/\ \_\ 
   \/_/ \/_/\/___/  \/_/ 

+------------------------------------------------+
|               Commands                         |
| Command          | Description                 |  
| use              | Use a module                |
| help             | Show available commands.    |
| exit             | Finish the script.          |
| update           | Update the script.          |
| show all         | Show all Modules.           |
| add              | Add the tool to the terminal|
+------------------------------------------------+

/\  _`\ /\ \            /\_ \  /\_ \     
\ \,\L\_\ \ \___      __\//\ \ \//\ \    
 \/_\__ \\ \  _ `\  /'__`\\ \ \  \ \ \   
   /\ \L\ \ \ \ \ \/\  __/ \_\ \_ \_\ \_ 
   \ `\____\ \_\ \_\ \____\/\____\/\____|
    \/_____/\/_/\/_/\/____/\/____/\/____/

"""


allmodules="""

+----------------------------------+  +------------------------------------+  +---------------------------------------+
|       Android Payloads           |  |          Windows Payloads          |  |        Linux Payloads                 |
|                                  |  | windows/meterpreter/reverse_tcp    |  | linux/x86/meterpreter/reverse_tcp     |
| android/meterpreter/reverse_tcp  |  |                                    |  |                                       |
|                                  |  | windows/meterpreter/reverse_http   |  | linux/x86/meterpreter_reverse_http    |
| android/meterpreter/reverse_http |  |                                    |  |                                       |
|==================================|  |  python/meterpreter/reverse_tcp    |  | linux/x64/meterpreter/reverse_tcp     |
|           Netcat                 |  |====================================|  |                                       |
|   android/shell/reverse_tcp      |  |            Netcat                  |  | linux/x64/meterpreter_reverse_http    |
|                                  |  |    windows/shell/reverse_tcp       |  |                                       |
|   android/shell/reverse_http     |  |                                    |  |  python/meterpreter/reverse_tcp       |
+----------------------------------+  |    windows/shell/reverse_udp       |  |=======================================|
                                      |                                    |  |              Netcat                   |
                                      |    python/shell_reverse_tcp        |  |      python/shell_reverse_tcp         |
                                      +------------------------------------+  +---------------------------------------+
"""    
ban="""

 /$$      /$$            /$$$$$$       /$$$$$$  /$$                 /$$ /$$
| $$$    /$$$           /$$__  $$     /$$__  $$| $$                | $$| $$
| $$$$  /$$$$  /$$$$$$$| $$  \__/    | $$  \__/| $$$$$$$   /$$$$$$ | $$| $$
| $$ $$/$$ $$ /$$_____/| $$$$ /$$$$$$|  $$$$$$ | $$__  $$ /$$__  $$| $$| $$
| $$  $$$| $$|  $$$$$$ | $$_/|______/ \____  $$| $$  \ $$| $$$$$$$$| $$| $$
| $$\  $ | $$ \____  $$| $$           /$$  \ $$| $$  | $$| $$_____/| $$| $$
| $$ \/  | $$ /$$$$$$$/| $$          |  $$$$$$/| $$  | $$|  $$$$$$$| $$| $$
|__/     |__/|_______/ |__/           \______/ |__/  |__/ \_______/|__/|__/
                                                                           
"""
# Checa el usuario

user = os.getlogin()
os.system("clear")
green()
print(ban)
print("Welcome "+user+"! Use help")

# Script principal

def tool_2():
    red()
    print(" ")
    opc = input("root@"+user+":~# ")

    if opc == "show all":
        os.system("clear")
        blue()
        print(ban)
        print(allmodules)
        tool_2()

    if opc == "help":
        os.system("clear")
        blue()
        print(help)
        tool_2()

    if opc == "update":
        os.system("Updating...")
        os.system("git pull")
        os.system("Done!!")
        exit()
    
    if opc == "use":
        os.system("clear")
        blue()
        print(ban)
        red()
        print("[X] Please specify a module. Example: use android/meterpreter/reverse_tcp")
        red()
        tool_2()

    if opc == "exit":
        os.system("rm -rf __pycache__")
        print("Good Bye!")
        exit()

    if opc == "use android/meterpreter/reverse_tcp":
        and_tcp()
        os.system("clear")
        green()
        print(ban)
        tool_2()

    if opc == "use android/meterpreter/reverse_http":
        and_http()
        os.system("clear")
        green()
        print(ban)
        tool_2()

    if opc == "use windows/meterpreter/reverse_tcp":
        wind_tcp()
        os.system("clear")
        green()
        print(ban)
        tool_2()

    if opc == "use windows/meterpreter/reverse_http":
        wind_http()
        os.system("clear")
        green()
        print(ban)
        tool_2()

    if opc == "use python/meterpreter/reverse_tcp":
        wind_py()
        os.system("clear")
        green()
        print(ban)
        tool_2()

    if opc == "use linux/x86/meterpreter/reverse_tcp":
        li86_tcp()
        os.system("clear")
        green()
        print(ban)
        tool_2()

    if opc == "use linux/x86/meterpreter/reverse_http":
        li64_http()
        os.system("clear")
        green()
        print(ban)
        tool_2()

    if opc == "use linux/x64/meterpreter/reverse_tcp":
        li64_tcp()
        os.system("clear")
        green()
        print(ban)
        tool_2()
        
    if opc == "use_linux python/meterpreter/reverse_tcp":
        li_py()
        os.system("clear")
        green()
        print(ban)
        tool_2()

    if opc == "use android/shell/reverse_http":
        and_net_http()
        os.system("clear")
        green()
        print(ban)
        tool_2()

    if opc == "use android/shell/reverse_tcp":
        and_net_tcp()
        os.system("clear")
        green()
        print(ban)
        tool_2()

    if opc == "use windows/shell/reverse_http":
        win_net_http()
        os.system("clear")
        green()
        print(ban)
        tool_2()

    if opc == "use windows/shell/reverse_tcp":
        win_net_tcp()
        os.system("clear")
        green()
        print(ban)
        tool_2()

    if opc == "use windows/shell/reverse_udp":
        win_net_udp()
        os.system("clear")
        green()
        print(ban)
        tool_2()

    if opc == "use python/shell_reverse_tcp":
        li_net_py()
        os.system("clear")
        green()
        print(ban)
        tool_2()


if __name__ == '__main__':
    try:
        os.system("clear")
        green()
        print(ban)
        tool_2()

    except(KeyboardInterrupt):
        print("\nCTRL+C Detected!, force program to stop\n")
        print("Good bye")
        os.system("rm -rf __pycache__")
        exit()

        
# SCRIPT HECHO POR GEERXOS ASI QUE SI COPIAS Y PEGAS DAME LOS CREDITOS CORRESPONDIENTES KID XD