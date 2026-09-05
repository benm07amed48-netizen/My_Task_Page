# Welcome to work again 

import sys
import tool

tool.new_user()
tool.instruction()
tool.logs()

instr={

    "l":["todo","done"],
    "e":["info","stat"],
    "a":"",
    "d":"",
    "i":""
}

if len (sys.argv)>1:
    command=sys.argv[1:]
else:
    command=input(": _ ").strip().strip("_").strip(".").split(" ")
    print(type(command))
tool.act(command)

else:
    print ("You didnn't input a validate command or misspelled it check the instruction agian") 
