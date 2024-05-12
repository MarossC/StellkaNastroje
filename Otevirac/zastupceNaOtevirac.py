from win32com.client import Dispatch
import os, time, sys

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


path = "C:\\Users\\"+ os.getlogin() +"\\Desktop\\Otevirac.lnk"  #This is where the shortcut will be created
wDir = os.path.dirname(os.path.realpath(__file__))
target = wDir + "\\otevirac.py" # directory to which the shortcut is created

shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.save()


print(sys.executable + "\n\n\n")
input("Enter pro smazani scriptu")
os.remove(os.path.abspath(__file__))
