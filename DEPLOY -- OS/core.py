import os
import time as t
import sys
import ctypes

promb = "<-> "

def list(cmd):
    if cmd == 'list':
        #You can to read in the file "commands.txt"
        print("exit        -- exit from program \ncls         -- clear the terminal \nlist        -- lists of commands\nhome        -- going the start program")
    elif cmd == 'exit':
        sys.exit(0)
    elif cmd == 'cls':
        global cls
        cls()
    elif cmd == 'home':
        cls()
        menu()
    else:
        print("\033[31mIncorrect command\033[32m")       
    
def cls():
    if os.name == 'nt':
       os.system('cls')
    else:
        os.system('clear')

def menu():
    ctypes.windll.kernel32.SetConsoleTitleW("DEPLOY -- OS")
    print("\033[32m|----------------------------|\n|           deploy           |\n|----------------------------|")
    print("Enter the command (You can help in the list of commands --> list)")
    while True:
        command = input(promb)
        list(command)