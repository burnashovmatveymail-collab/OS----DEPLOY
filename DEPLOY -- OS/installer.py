import os
import time as t
import sys
import ctypes

def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#START:
def start():
    ctypes.windll.kernel32.SetConsoleTitleW("DEPLOY -- OS INSTALLER")
    cls()
    if os.path.exists("Connector.py"):
        print("---- 20%")
    else:
        print("ERROR -- YOU NOT HAVE TO THE ALL MATERIAL")
        t.sleep(5)
        sys.exit(0)

    t.sleep(1)
    cls()

    if os.path.exists("core.py"):
        print("-------- 40%")
    else:
        print("ERROR -- YOU NOT HAVE TO THE ALL MATERIAL")
        t.sleep(5)
        sys.exit(0)

    t.sleep(1)
    cls()

    if os.path.exists("commands.txt"):
        print("------------ 60%")
        t.sleep(1)
    else:
        print("!! You not have the commands list for the OS !!")
        t.sleep(5)

    cls()

    if os.path.exists("code.py"):
        print("--------------- 80%")
    else:
        print("ERROR -- YOU NOT HAVE TO THE ALL MATERIAL")
        t.sleep(5)
        sys.exit(0)

    t.sleep(1)
    cls()

    if os.path.exists("license.txt"):
        print("\033[32m-------------------- 100%")
    else:
        print("ERROR -- YOU NOT HAVE TO THE ALL MATERIAL")
        t.sleep(5)
        sys.exit(0)

    t.sleep(1)
    cls()

    print('DONE!!\n$$You have the connector, core, installer, license, lists of commands and key for Starting OS.$$')
    t.sleep(3)
    cls()