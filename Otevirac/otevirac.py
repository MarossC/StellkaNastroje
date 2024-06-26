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


config = 'mconfig.cfg'
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


def interpreter(line):
    proc = subprocess.Popen(line, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = proc.communicate()
    return out.decode()

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


# - - - - Windows 10/11 detekce
wmic = interpreter("wmic os get name")
wmicos = wmic.split("\n")
version = wmicos[1].split(" ")

if version[2] == "11":
    IsWinEleven = True
else:
    IsWinEleven = False

# - - - - Inputy
print("Stellaria Otevirac [Version 69.420.6489918.89179]")
print("(c) Maros Corporation. All rights reserved.")
print("\n\n")

# - - config check
global bConfig, pocetCele, pocetTrictvrt, pocetPulka, pocetMining, pocetMicro
bConfig = False
if os.path.isfile(config):
    f = open(config, 'r')
    line = f.readlines()
    f.close()
    while True:
        inputConfig = input("Chceš načíst staré okna? (y/n): ")
        if inputConfig == "y" or inputConfig == "Y":
            bConfig = True
            pocetCele = int(line[0])
            pocetTrictvrt = int(line[1])
            pocetPulka = int(line[2])
            pocetMining = int(line[3])
            pocetMicro = int(line[4])
            break
        elif inputConfig == "n" or inputConfig == "N":
            bConfig = False
            break
        else:
            print("Nezadal jsi Y nebo N.\n")

print("\n")
# - - Cele okna
if not bConfig:
    while True:
        inputCele = input("Pocet celych oken (100%/100%): ")
        if inputCele == "":
            inputCele = 0
        try:
            pocetCele = int(inputCele)
            break
        except ValueError:
            print("Zkus to znova, nezadal jsi cislo.\n")

    # - - Trictvrtecni okna

    while True:
        inputTrictvrt = input("Pocet trictvrtecnich oken (100%/75%): ")
        if inputTrictvrt == "":
            inputTrictvrt = 0
        try:
            pocetTrictvrt = int(inputTrictvrt)
            break
        except ValueError:
            print("Zkus to znova, nezadal jsi cislo.\n")

    # - - Polovicni okna

    while True:
        inputPulka = input("Pocet polovicnich oken (100%/50%): ")
        if inputPulka == "":
            inputPulka = 0
        try:
            pocetPulka = int(inputPulka)
            break
        except ValueError:
            print("Zkus to znova, nezadal jsi cislo.\n")

    # - - Normal kopaci okna

    while True:
        inputMining = input("Pocet normal kopacich oken (50%/50%): ")
        if inputMining == "":
            inputMining = 0
        try:
            pocetMining = int(inputMining)
            break
        except ValueError:
            print("Zkus to znova, nezadal jsi cislo.\n")

    # - - Mikro kopaci okna

    while True:
        inputMicro = input("Pocet malych kopacich oken (50%/25%): ")
        if inputMicro == "":
            inputMicro = 0
        try:
            pocetMicro = int(inputMicro)
            break
        except ValueError:
            print("Zkus to znova, nezadal jsi cislo.\n")

# - - - - Otevirani

print("Pockej nez se otevrou okna.")

f = open(config, 'w')
f.write(str(pocetCele) + "\n")
f.write(str(pocetTrictvrt) + "\n")
f.write(str(pocetPulka) + "\n")
f.write(str(pocetMining) + "\n")
f.write(str(pocetMicro) + "\n")
f.close()

# - 30px bar okna, 50px W11 taskbar, 40px W10 taskbar

# - - Cele okna
if pocetCele > 0:
    setWidth(9999)
    setHeight(9999)

    while pocetCele > 0:
        subprocess.Popen([gameexe])
        pocetCele = pocetCele - 1

    time.sleep(8)

# - - Trictvrtecni okna
if pocetTrictvrt > 0:
    setWidth(int(round(s_width * 0.75)))
    if IsWinEleven:
        setHeight(int(s_height - 80))
    else:
        setHeight(int(s_height - 70))

    while pocetTrictvrt > 0:
        subprocess.Popen([gameexe])
        pocetTrictvrt = pocetTrictvrt - 1

    time.sleep(8)

# - - Polovicni okno
if pocetPulka > 0:
    setWidth(int(s_width / 2))
    if IsWinEleven:
        setHeight(int(s_height - 80))
    else:
        setHeight(int(s_height - 70))

    while pocetPulka > 0:
        subprocess.Popen([gameexe])
        pocetPulka = pocetPulka - 1

    time.sleep(8)

# - - Normalni Kopacske okno
if pocetMining > 0:
    setWidth(int(s_width / 2))
    if IsWinEleven:
        setHeight(int((s_height - 110) / 2))
    else:
        setHeight(int((s_height - 100) / 2))    

    while pocetMining > 0:
        subprocess.Popen([gameexe])
        pocetMining = pocetMining - 1

    time.sleep(8)

# - - Micro Kopacske okno
if pocetMicro > 0:
    setWidth(int(s_width / 4))
    if IsWinEleven:
        setHeight(int((s_height - 110) / 2))
    else:
        setHeight(int((s_height - 100) / 2)) 
    
    while pocetMicro > 0:
        subprocess.Popen([gameexe])
        pocetMicro = pocetMicro - 1





