#!/usr/bin/python
import os
#| |__   __ _  ___| | _(_)_ __   __ _  | |__  _   _    ___  __ _ ___ _   _ 
#| '_ \ / _` |/ __| |/ / | '_ \ / _` | | '_ \| | | |  / _ \/ _` / __| | | |
#| | | | (_| | (__|   <| | | | | (_| | | |_) | |_| | |  __/ (_| \__ \ |_| |
#|_| |_|\__,_|\___|_|\_\_|_| |_|\__, | |_.__/ \__, |  \___|\__,_|___/\__, |
#                               |___/         |___/                  |___/ 
                     
#__      ____ _ _   _ 
#\ \ /\ / / _` | | | |
 #\ V  V / (_| | |_| |
  #\_/\_/ \__,_|\__, |
   #            |___/ 
print "     type  option and type ip after your choose"
print "-s to scan ip by nmap"
print "-w to attack wifi"
print "-c to create wordlist to passwords"
print "-h to help and waht's programs we use"
print "-m to make payloads in metasploit"
                                                   
#####  #   #      ##   #    # #    # ###### #####  
#    #  # #      #  #  #    # ##  ## #      #    # 
#####    #      #    # ###### # ## # #####  #    # 
#    #   #      ###### #    # #    # #      #    # 
#    #   #      #    # #    # #    # #      #    # 
#####    #      #    # #    # #    # ###### #####  
                                                   
                                          
#    #   ##    ####   ####    ##   #    # 
#    #  #  #  #      #       #  #  ##   # 
###### #    #  ####   ####  #    # # #  # 
#    # ######      #      # ###### #  # # 
#    # #    # #    # #    # #    # #   ## 
#    # #    #  ####   ####  #    # #    # 
x = raw_input("choose: ")
if x == "-s":
   y = raw_input("ip: ")
   os.system("nmap -v"+y)
elif x == "-w":
   os.system("wifite")
elif x == "-c":
   os.system("crunch")
elif x == "-h":
   print "-s=nmap -w=wifite -c=crunch -m=metasploit(msfconsole)"
elif x == "-m":
    os.system("msfconsole")
else:
   print " wrong chosse try again"


