import sys
#import tkinter
from tkinter import *
from termcolor import colored

#CREATE TKINTER INSTANCE
root = tkinter.Tk()
root.withdraw()

#INPUT COMMAND
action = input("> ").lower()

#IF ACTION="EXIT" || "QUIT" || EMPTY → QUIT INTERFACE
while (action != "exit") and (action != "quit") and (action != "") and (action != " "):
    #ADD_MODULE
    if action == "add_module":
        module_name = tkinter.Entry(root)
        file_path = filedialog.askopenfilename()
        print("::: Module name: " + colored(file_path, 'green'))
        print("::: Module path: " + colored(file_path, 'green'))
    
    #ELSE
    else:
        print("::: " + colored("Cannot find \'" + action + "\'", 'red'))

    #INPUT COMMAND
    action = input("> ").lower()