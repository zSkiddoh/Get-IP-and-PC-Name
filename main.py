#Made By zSkiddoh
#Date Creation: 28/10/2021

import socket
from colorama import Fore, init
import os
import time
init()

os.system("cls")

print(Fore.GREEN + "Buscando Información..")
time.sleep(7)

os.system("cls")

print(Fore.GREEN + "¡Información Encontrada!")

pc = socket.gethostname() 

ip = socket.gethostbyname(pc) 

print("")
print(Fore.WHITE + "El nombre de tu PC es: " + Fore.RED + pc) 
print(Fore.WHITE + "La IP de tu PC es: " + Fore.RED + ip)
print("")
print(Fore.GREEN + "¡Un saludo crack!")
