#animacion
import sys
import time
def anim():
     lowerstr= "metasploit shell by geerxos"
     upperstr = lowerstr.upper()
     for x in range(len(lowerstr)):
          s = '\r' + lowerstr[0:x] + upperstr[x] + lowerstr[x+1:] + '\r'
          sys.stdout.write(s)
          sys.stdout.flush()
          time.sleep(0.1)
