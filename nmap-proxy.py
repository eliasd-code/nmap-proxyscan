import os
import time
import sys
os.system("clear")
print("------------------------------------------------------------------------------------")
print("!!!!ACHTUNG!!!!\nVERGEWISSERE DICH DAS DU ROOT BIST!(sudo su)\n!!!!ACHTUNG!!!!")
os.system("id")
print("------------------------------------------------------------------------------------")
print("by eliasd")
print("https://github.com/eliasd-code")
print("")
print("gebe die Ports ein die gescannt werden sollen")
print("mind. ein Port muss angegeben sein!")
print("wenn du fertig bist gibst du die 0 ein")
anzahl=0
liste=[]
while True:
    anzahl += 1
    print(anzahl,"Port :")
    ports=(input(":"))
    if ports == "0":
        break
    else:
        liste.append(ports)

# Ausgabe
print("")
print("Folgende Ports werden gescannt "+str(liste))
print("")
print("gebe die IP ein :")  # IP
ip=(input())
print("")
print("gebe die Schalter ein (-sS,-Pn usw)")    # Schalter
schalter=input()
print("")
print("die Eingabe ist : \nproxychains nmap "+str(schalter)+" -p "+str(liste)+" "+str(ip))
print("")
print("Blende die Klammern einfach aus, die werden nicht mit ausgeführt")
os.system("service tor start")
rf=input("richtig ? (ja,nein): ")
if rf == "ja":
    os.system("clear")
    print("Okay")
    print("")
    print("----------------------------------------------")
    print("Deine Ip ist")
    os.system("torsocks curl -s https://api.ipify.org")
    print("")
    print("----------------------------------------------")
    os.system("service tor restart")
    print("")
    time.sleep(5)
    print("Deine Neue IP ist")
    os.system("torsocks curl -s https://api.ipify.org")
    print("\n")
    print("----------------------------------------------")
    print("")
    print("----------------------------------------------")
    for element in liste:
        print("Scann Port:",element)
        os.system("proxychains nmap -oA scan "+schalter+" -p "+element+" "+ip)
        # neue IP
        print("")
        print("Neue IP.....")
        os.system("service tor restart")
        time.sleep(5)
        print("Deine Neue IP ist")
        os.system("torsocks curl -s https://api.ipify.org")
        print("\n----------------------------------------------")
            
        # Log Datei 
        os.system("cat scan.nmap >> nmap-proxy-scan.log")
        os.system("rm -r scan.xml && rm -r scan.nmap && rm -r scan.gnmap")
        os.system("chmod +x nmap-proxy-scan.log")

else:
    print("nein.. Okay")
