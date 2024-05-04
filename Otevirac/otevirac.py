import os
import re
import time
import subprocess
import ctypes
import sys
from ctypes import windll


try:
    is_admin = ctypes.windll.shell32.IsUserAnAdmin()
except:
    is_admin = False

if not is_admin:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

gameexe = 'start.exe'
gameconfig = 'settings.cfg'

# check if files exist
if os.path.isfile(gameexe) and os.path.isfile(gameconfig):
    print("")
    pass
else:
    print("Script neni ve slozce s Stellarii. Presun do slozky se hrou, a zkus znova.")
    time.sleep(15)
    exit()


user32 = windll.user32
s_width = user32.GetSystemMetrics(0)
s_height = user32.GetSystemMetrics(1)


def setWidth(fWidth):
    with open(gameconfig, 'r+') as f:
        filedata = f.read()
        pattern = r"(WIDTH)\s+(\d+)"
        replacement = r"\1 {}" .format(fWidth)
        newdata = re.sub(pattern, replacement, filedata)
        f.seek(0)
        f.write(newdata)
        f.close()

def setHeight(fHeight):
    with open(gameconfig, 'r+') as f:
        filedata = f.read()
        pattern = r"(HEIGHT)\s+(\d+)"
        replacement = r"\1 {}" .format(fHeight)
        newdata = re.sub(pattern, replacement, filedata)
        f.seek(0)
        f.write(newdata)
        f.close()

# - - - - Inputy

# - - Cele okna
while True:
    inputCele = input("Pocet celych oken: ")
    if inputCele == "":
        inputCele = 0
    try:
        pocetCele = int(inputCele)
        break
    except ValueError:
        print("Zkus to znova, nezadal jsi cislo.\n")

# - - Polovicni okna

while True:
    inputPulka = input("Pocet polovicnich oken: ")
    if inputPulka == "":
        inputPulka = 0
    try:
        pocetPulka = int(inputPulka)
        break
    except ValueError:
        print("Zkus to znova, nezadal jsi cislo.\n")

# - - Normal kopaci okna

while True:
    inputMining = input("Pocet normal kopacich oken: ")
    if inputMining == "":
        inputMining = 0
    try:
        pocetMining = int(inputMining)
        break
    except ValueError:
        print("Zkus to znova, nezadal jsi cislo.\n")

# - - Mikro kopaci okna

while True:
    inputMicro = input("Pocet mikro kopacich oken: ")
    if inputMicro == "":
        inputMicro = 0
    try:
        pocetMicro = int(inputMicro)
        break
    except ValueError:
        print("Zkus to znova, nezadal jsi cislo.\n")

# - - - - Otevirani

print("Pockej nez se otevrou okna.")

# - - Cele okna

setWidth(9999)
setHeight(9999)

while pocetCele > 0:
    subprocess.Popen([gameexe])
    pocetCele = pocetCele - 1

time.sleep(3)

# - - Polovicni okno

setWidth(s_width / 2)
setHeight(s_height - 80)

while pocetPulka > 0:
    subprocess.Popen([gameexe])
    pocetPulka = pocetPulka - 1

time.sleep(3)

# - - Normalni Kopacske okno

setHeight((s_height - 110) / 2)

while pocetMining > 0:
    subprocess.Popen([gameexe])
    pocetMining = pocetMining - 1

time.sleep(3)

# - - Micro Kopacske okno

setWidth(s_width / 4)
setHeight((s_height - 90) / 2)

while pocetMicro > 0:
    subprocess.Popen([gameexe])
    pocetMicro = pocetMicro - 1

print("\n")
print("####################")
print("#### By  Maross ####")
print("####################")
time.sleep(2)
