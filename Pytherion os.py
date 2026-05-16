import time
import socket
import cpuinfo
import datetime
import requests
import psutil
import os
from autocorrect import Speller


print ("""

██████╗░██╗░░░██╗████████╗██╗░░██╗███████╗██████╗░██╗░█████╗░███╗░░██╗  ░█████╗░░██████╗
██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║██╔════╝██╔══██╗██║██╔══██╗████╗░██║  ██╔══██╗██╔════╝
██████╔╝░╚████╔╝░░░░██║░░░███████║█████╗░░██████╔╝██║██║░░██║██╔██╗██║  ██║░░██║╚█████╗░
██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║██╔══╝░░██╔══██╗██║██║░░██║██║╚████║  ██║░░██║░╚═══██╗
██║░░░░░░░░██║░░░░░░██║░░░██║░░██║███████╗██║░░██║██║╚█████╔╝██║░╚███║  ╚█████╔╝██████╔╝
╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░╚════╝░╚═╝░░╚══╝  ░╚════╝░╚═════╝░
""")
time.sleep(1)
print ("Starting os")
ram = psutil.virtual_memory().total
host_name = socket.gethostname ()
cpu_name = cpuinfo.get_cpu_info()

print ("Ram :",ram)
time.sleep(1)
print("Pytherion OS v1.0")
time.sleep (1)
print ("Welcome")

while True:
    command = input("pytherionos> ")

    if command == 'sysinfo':
        print ("Pytherion OS v1.0")
        print ("installed ram: ",round(ram / (1024**3),2),"GB")

    elif command=='calculator':

        try:

            A=float(input("Enter a number"))
            B=float(input("Enter another number"))

        except ValueError:
            print("Error please write valid numbers")
            continue
        
        op=input("Enter an oprator(+,-,x,/)")
        if op=="+":
            print (A,"+",B,"=",A+B)
            print ("finish")
        elif op =="-":
            print (A,"-",B,"=",A-B)
            print ("finish")
        elif op =="x":
            print (A,"x",B,"=",A*B)
            print ("finish")
        elif op == "/":
            
            if B==0:
                print("Cannot be divided by zero")
            else:
                print (A,"/",B,"=",A/B)


        else:
            print ("invalid oprator")

    elif command=='pyfetch':
        print ("""

██████╗░██╗░░░██╗████████╗██╗░░██╗███████╗██████╗░██╗░█████╗░███╗░░██╗  ░█████╗░░██████╗
██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║██╔════╝██╔══██╗██║██╔══██╗████╗░██║  ██╔══██╗██╔════╝
██████╔╝░╚████╔╝░░░░██║░░░███████║█████╗░░██████╔╝██║██║░░██║██╔██╗██║  ██║░░██║╚█████╗░
██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║██╔══╝░░██╔══██╗██║██║░░██║██║╚████║  ██║░░██║░╚═══██╗
██║░░░░░░░░██║░░░░░░██║░░░██║░░██║███████╗██║░░██║██║╚█████╔╝██║░╚███║  ╚█████╔╝██████╔╝
╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░╚════╝░╚═╝░░╚══╝  ░╚════╝░╚═════╝░
""")
        print ("OS: Pytherion OS")
        print("Host:",host_name)
        print ("Memory:",round(ram / (1024**3),2),"GB")
        print (f"Cpu: {cpu_name['brand_raw']}")
    elif command=='help':
        print ("""
Available commands
sysinfo: shows system info
calculator: opens calculator
pyfetch : linux neofetch like system information
web: searches the web(beta)
exit:shuts down the terminal               
""")
    elif command =='date':
        print(datetime.date.today())
    elif command =='time':
        print (time.strftime("%H:%M"))
    elif command =='web':
        print("Search the web (type 'exit' to quit)\n")
        spell = Speller(lang='en')
        while True:
            q = input("Type to search: ")
            if q.lower() == "exit": break
            cq=spell(q)

            r = requests.get(
                "https://api.duckduckgo.com/", 
                params={
                    "q": cq,
                    "format":"json"
                },
            headers={
                "User-Agent": "Mozilla/5.0"
                }
            ).json()
            t = [f"{i['Text']} - {i['FirstURL']}" for i in r.get("RelatedTopics", []) if 'Text' in i][:5]
            print("\n".join(t or ["No results found."]), "\n")

    elif command=='exit':
        print ("Shutting down..")
        time.sleep(1)
        exit()
    else:
        print("Unknown Command type 'help'")   
