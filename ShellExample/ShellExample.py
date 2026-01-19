# MxCovert06

import os
import textwrap
def clear():
    print("\033[H\033[2J", end="")

# 1: Having constant user input checking
clear()
print("Welcome to Pyshell. Type 'PyHelp' for a brief explanation")
while True:
    try:    
#       Have current directory in shell
        dir = os.getcwd()
        current_dir = dir.split(os.path.sep)
#       print(current_dir[-1])
        
        usercmd = input(f"/{current_dir[-1]} || PyShell$> ")
        clean_input = usercmd.strip()
        listed_input = clean_input.split(" ")
        if len(listed_input) == 0:
            continue
        command = listed_input[0].lower()
        args = listed_input[1:]

#       print(command)
#       print(f"Arguments: {args}")
        if command == "pyhelp":
            help = "PyShell is a small python-based shell capable of running native commands. While not used as an individual shell, it serves as a teaching tool for the OS module and user input logic."
            cmds = ["CLEAR"]

            wrapped_help = textwrap.fill(help, width=50)
            print(f"\n{wrapped_help}\n")
            print(f"Currently these commands are supported:\n")
            for cmd in cmds:
                print(f"{cmd}\n") # List all commands   
            continue
        elif command == "clear":
            clear()
            continue
        else:
            responseOS = os.system(f"{usercmd} 2>nul")
            if responseOS != 0:
                print("Your system cannot run this command")
                
   
                
        
    except KeyboardInterrupt:
        print("Exiting Shell...")
        break