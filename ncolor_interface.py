#IMPORTS
import sys
import glob
import os

#IMPORTANT VARIABLES
modules = []

#LOAD ALL RECENT MODULES
with open('modules.save') as f:
    modules = f.read().splitlines()

#IMPORTANT VARIABLES
save_file = open("modules.save", "w+")

#FUNCTIONS
#PRINT
def p (text, important = False):
    if important:
        print("::: " + text)
  
    else:
        print(": " + text)

#INPUT 
def i (text, important = False):
    if important:
        ret = input("::: " + text)
  
    else:
        ret = input(": " + text)
        
    return ret

#CONTROL MODULE
def control_module (module_name):
    mod_files = []

    for m in os.listdir("modules/" + module_name):
        mod_files.append(m.lower())

    if len(mod_files) >= 3:
        if "module" in mod_files:
            if "get.py" in mod_files:
                if "test.py" in mod_files:
                    return True    
                return False
            return False
        return False
    return False

def modules_save ():
    save_file.truncate()

    for m in modules:
        save_file.write(m + "\n")

def get (module):
    if control_module(module):
        return os.popen("python3 modules/" + module + "/get.py").read()
    else:
        return "NO MODULE"

def test (module):
    if control_module(module):
        return os.popen("python3 modules/" + module + "/test.py").read()
    else:
        return "NO MODULE"

def put (module, arg):
    if control_module(module):
        return os.popen("python3 modules/" + module + "/put.py " + arg).read()
    else:
        return "NO MODULE"

#INTERFACE
#INPUT COMMAND
action = input("> ").lower()

#IF ACTION= "EXIT" || "QUIT" || EMPTY -> QUIT INTERFACE
while (action != "exit") and (action != "quit") and (action != "") and (action != " "):
    #DISPLAY MODULES
    if action == "display":
        for mod_dir in os.listdir("modules"):
            p(mod_dir)
        
        p("Length: " + str(len(os.listdir("modules"))), True)

    #LOAD MODULES
    elif action == "load":
        if i("Load all modules? [y/n] : ", True).lower() == "y":
            for mod_dir in os.listdir("modules"):
                if (control_module(mod_dir)) and (mod_dir not in modules):
                    modules.append(mod_dir)
                    p("Added \'" + mod_dir + "\' module")

    #ADD MODULE
    elif action == "add":
        list_modules = []
        
        for mod_dir in os.listdir("modules"):
                if control_module(mod_dir):
                    list_modules.append(mod_dir)

        for inc in range(len(list_modules)):
            p("[" + str(inc) + "]: " + list_modules[inc])
        
        addID = int(i("Insert ID of module which should be added: ", True))

        if (addID >= 0) and (addID < len(list_modules)):
            if (i("Add module \'" + list_modules[addID] + "\'? [y/n] : ", True).lower() == "y") and (list_modules[addID] not in modules):
                modules.append(list_modules[addID])
                p("Added new module \'" + list_modules[addID] + "\'", True)

            else:
                p("Cancelled adding module", True)
    
    #DISPLAY OPENED MODULES
    elif (action == "modules") or (action == "mod"):
        for inc in range(len(modules)):
            p("[" + str(inc) + "]: " + modules[inc])
            
        p("Length: " + str(len(modules)), True)
    
    #REMOVE MODULE
    elif (action == "remove") or (action == "rm"):
        for inc in range(len(modules)):
            p("[" + str(inc) + "]: " + modules[inc])
            
        rmID = int(i("Insert ID of module which should be removed: ", True))
        
        if (rmID >= 0) and (rmID < len(modules)):
            if i("Remove module \'" + modules[rmID] + "\'? [y/n] : ", True).lower() == "y":
                p("Removed module \'" + modules[rmID] + "\'", True)
                modules.remove(modules[rmID])

            else:
                p("Cancelled removing module \'" + module_name + "\'", True)

        else:
            p("Cancelled removing modules", True)
    
    #GET
    elif action.split(' ')[0] == "get":
        if len(action.split(' ')) > 1:
            getID = int(action.split(' ')[1])

            if (getID >= 0) and (getID < len(modules)):
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
        p("DISPLAY", True)
        p("Display all modules")
        p("MODULES, MOD", True)
        p("Print all opened modules")
        p("LOAD", True)
        p("Load all modules")
        p("ADD", True)
        p("Add specific module")
        p("REMOVE, RM", True)
        p("Remove specific module")
        p("GET [ID]", True)
        p("Read value from module")
        p("TEST [ID]", True)
        p("Test if module works properly")
        p("PUT [ID] [ARGUMENT]", True)
        p("Pass argument to module")
        p("CLEAR", True)
        p("Clear terminal")
        p("HELP", True)
        p("Display help dialog")
        p("EXIT, QUIT", True)
        p("Quit and save interface")

    #ELSE
    else:
        p("Cannot find \'" + action + "\'", True)

    action = input("> ").lower()

modules_save()