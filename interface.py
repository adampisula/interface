#IMPORTS
import sys
import glob
import os
import importlib

#IF EXISTS IMPORT TERMCOLOR
termcolor_loader = importlib.find_loader('termcolor')
tc_available = termcolor_loader is not None

if tc_available:
    from termcolor import colored

#IMPORTANT VARIABLES
modules = []

#LOAD ALL RECENT MODULES
with open(os.path.dirname(os.path.abspath(__file__)) + '/modules.save') as f:
    modules = f.read().splitlines()

#IMPORTANT VARIABLES
save_file = open(os.path.dirname(os.path.abspath(__file__)) + "/modules.save", "w+")

#FUNCTIONS
#PRINT
def p (text, important = False):
    if len(sys.argv) > 1:
        print(text)

    else:        
        if important:
            if tc_available:
                print("::: " + colored(text, "green"))
            else:
                print("::: " + text)
    
        else:
            if tc_available:
                print(": " + colored(text, "yellow"))
            else:
                print(": " + text)

#INPUT 
def i (text, important = False):
    if important:
        if tc_available:
            ret = input("::: " + colored(text, "green"))
        else:
            ret = input("::: " + text)

    else:
        if tc_available:
            ret = input(": " + colored(text, "yellow"))
        else:
            ret = input(": " + text)
        
    return ret

#CONTROL MODULE
def control_module (module_name):
    mod_files = []

    for m in os.listdir(os.path.dirname(os.path.abspath(__file__)) + "/modules/" + module_name):
        mod_files.append(m.lower())

    if len(mod_files) >= 4:
        if "module" in mod_files:
            if "get.py" in mod_files:
                if "test.py" in mod_files:
                    if "put.py" in mod_files:
                        return True
                    return False    
                return False
            return False
        return False
    return False

def modules_save ():
    save_file.truncate()

    for m in modules:
        save_file.write(m + "\n")

def get (module, arg = ""):
    if control_module(module):
        return os.popen("python3 " + os.path.dirname(os.path.abspath(__file__)) + "/modules/" + module + "/get.py " + arg).read()
    else:
        return "NO MODULE"

def test (module):
    if control_module(module):
        return os.popen("python3 " + os.path.dirname(os.path.abspath(__file__)) + "/modules/" + module + "/test.py").read()
    else:
        return "NO MODULE"

def put (module, arg):
    if control_module(module):
        return os.popen("python3 " + os.path.dirname(os.path.abspath(__file__)) + "/modules/" + module + "/put.py " + arg).read()
    else:
        return "NO MODULE"

#INTERFACE
#INPUT COMMAND
action = ""

action_inc = 1

#IF IN ONE-USE MODE SPLIT SYS.ARGV
if (len(sys.argv) > 1) and (sys.argv[len(sys.argv) - 1] != "-s"):
    #if sys.argv[1] != "-s":
    for inc in range(1, len(sys.argv) - 1):
        action += sys.argv[inc] + " "

    action += sys.argv[len(sys.argv) - 1]
    action = action.lower()

    commands = action.split("@")

    action = commands[0]
    action = action.strip()

#ELSE -> WAIT FOR COMMAND
else:
    action = input("> ").lower()

#IF ACTION= "EXIT" || "QUIT" || EMPTY -> QUIT INTERFACE
while (action != "exit") and (action != "quit") and (action != "") and (action != " "):
    #DISPLAY MODULES
    if action == "display":
        for mod_dir in os.listdir(os.path.dirname(os.path.abspath(__file__)) + "/modules"):
            if control_module(mod_dir):
                p(mod_dir)
        
        p("Length: " + str(len(os.listdir(os.path.dirname(os.path.abspath(__file__)) + "/modules"))), True)

    #LOAD MODULES
    elif action == "load":
        for mod_dir in os.listdir(os.path.dirname(os.path.abspath(__file__)) + "/modules"):
            if (control_module(mod_dir)) and (mod_dir not in modules):
                modules.append(mod_dir)
                p("Added \'" + mod_dir + "\' module")

    #ADD MODULE
    elif action.split(' ')[0] == "add":
        list_modules = []
            
        for mod_dir in os.listdir(os.path.dirname(os.path.abspath(__file__)) + "/modules"):
                if control_module(mod_dir):
                    list_modules.append(mod_dir)

        if len(action.split(' ')) > 1:
            addName = action.split(' ')[1].upper()

            if addName in list_modules:
                if addName not in modules:
                    modules.append(addName)
                    p("Added module \'" + addName + "\'", True)

            else:
                p("Cancelled adding module - no module named \'" + addName + "\'", True)

        else:
            for inc in range(len(list_modules)):
                p("[" + str(inc) + "]: " + list_modules[inc])

            addID = int(i("Insert ID of module which should be added: ", True))

            if (addID >= 0) and (addID < len(list_modules)):
                if (i("Add module \'" + list_modules[addID] + "\'? [y/n] : ", True).lower() == "y") and (list_modules[addID] not in modules):
                    if list_modules[addID] not in modules:
                        modules.append(list_modules[addID])
                        p("Added module \'" + list_modules[addID] + "\'", True)

                else:
                    p("Cancelled adding module", True)
    
    #DISPLAY OPENED MODULES
    elif (action.split(" ")[0] == "modules") or (action.split(" ")[0] == "mod"):
        for inc in range(len(modules)):
            if len(action.split(" ")) > 1:
                p(modules[inc])

            else:
                p("[" + str(inc) + "]: " + modules[inc])
            
        if len(action.split(" ")) == 1:
            p("Length: " + str(len(modules)), True)
    
    #REMOVE MODULE
    elif (action.split(' ')[0] == "remove") or (action.split(' ')[0] == "rm"):
        if len(action.split(' ')) > 1:
            rmName = action.split(' ')[1].upper()

            if rmName in modules:
                modules.remove(rmName)
                p("Removed module \'" + rmName + "\'", True)

            else:
                p("Cancelled removing module - no module named \'" + rmName + "\'", True)

        else:
            for inc in range(len(modules)):
                p("[" + str(inc) + "]: " + modules[inc])
                
            rmID = int(i("Insert ID of module which should be removed: ", True))
            
            if (rmID >= 0) and (rmID < len(modules)):
                if i("Remove module \'" + modules[rmID] + "\'? [y/n] : ", True).lower() == "y":
                    p("Removed module \'" + modules[rmID] + "\'", True)
                    modules.remove(modules[rmID])

                else:
                    p("Cancelled removing module \'" + modules[rmID] + "\'", True)

            else:
                p("Cancelled removing module", True)
    
    #GET
    elif action.split(' ')[0] == "get":
        if len(action.split(' ')) > 1:
            getID = int(action.split(' ')[1])

            if (getID >= 0) and (getID < len(modules)):
                if len(action.split(" ")) > 2:
                    p(get(modules[getID], action.split(" ")[2]))
                
                else:
                    p(get(modules[getID]))

        else:
            for inc in range(len(modules)):
                p("[" + str(inc) + "]: " + modules[inc])
                
            getID = int(i("Get ID: ", True))

            if (getID >= 0) and (getID < len(modules)):
                p(get(modules[getID]))

    #TEST
    elif action.split(' ')[0] == "test":
        if len(action.split(' ')) > 1:
            testID = int(action.split(' ')[1])

            if (testID >= 0) and (testID < len(modules)):
                p(test(modules[testID]))

        else:
            for inc in range(len(modules)):
                p("[" + str(inc) + "]: " + modules[inc])
                
            testID = int(i("Test ID: ", True))

            if (testID >= 0) and (testID < len(modules)):
                p(test(modules[testID]))

    #PUT
    elif action.split(' ')[0] == "put":
        if len(action.split(' ')) > 2:
            putID = int(action.split(' ')[1])
            putArg = ""

            for inc in range(2, len(action.split(' '))):
                putArg += action.split(' ')[inc] + " "

            if (putID >= 0) and (putID < len(modules)):
                p(put(modules[putID], putArg))

        elif len(action.split(' ')) > 1:
            putID = int(action.split(' ')[1])
            
            if (putID >= 0) and (putID < len(modules)):
                putArg = i("Insert argument to pass to \'" + modules[putID] + "\': ", True)

                p(put(modules[putID], putArg))

        else:
            for inc in range(len(modules)):
                p("[" + str(inc) + "]: " + modules[inc])
                
            putID = int(i("Put ID: ", True))

            if (putID >= 0) and (putID < len(modules)):
                putArg = i("Insert argument to pass to \'" + modules[putID] + "\': ", True)

                p(put(modules[putID], putArg))

    #CLEAR
    elif action == "clear":
        os.system("clear")

    #HELP
    elif action == "help":
        p("python3 interface.py [COMMAND]", True)
        p("python3 interface.py [COMMAND_1]@[COMMAND_2]@[COMMAND_3]", True)
        p("Running interface in one-use mode (without brackets)")
        print()
        p("DISPLAY", True)
        p("Display all modules")
        p("MODULES, MOD", True)
        p("Print all opened modules")
        p("LOAD", True)
        p("Load all modules")
        p("ADD [NAME]", True)
        p("Add specific module")
        p("REMOVE, RM [NAME]", True)
        p("Remove specific module")
        p("GET [ID] [ARGUMENTS]", True)
        p("Read value from module")
        p("TEST [ID]", True)
        p("Test if module works properly")
        p("PUT [ID] [ARGUMENTS]", True)
        p("Pass argument to module")
        p("CLEAR", True)
        p("Clear terminal")
        p("HELP", True)
        p("Display help dialog")
        p("EXIT, QUIT", True)
        p("Quit and save interface")

    #ELSE
    else:
        p("Cannot find \'" + action.split(' ')[0] + "\'", True)

    #IF IN ONE-USE MODE USE NEXT COMMAND
    if (len(sys.argv) > 1) and (sys.argv[len(sys.argv) - 1] != "-s"):
        if len(commands) == 1:
            action = ""
    
        else:
            if action_inc < len(commands):
                action = commands[action_inc]
                action = action.strip()

                action_inc += 1

                p("@")
            
            else:
                action = ""
    
    #ELSE -> WAIT FOR NEXT COMMAND
    else:
        action = input("> ").lower()

#SAVE ALL MODULES TO FILE BEFORE EXIT
modules_save()