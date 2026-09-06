# Welcome to work again 

import sys
import tool

tool.new_user()
tool.instruction()
tool.logs()

instr={

    "l":{
        "all":tool.l_all,
        "todo":tool.l_todo,
        "done":tool.l_done
        },
    "e":{
        "info":"",
        "stat":""
        },
    "a":"",
    "d":"",
    "i":""
}

if len (sys.argv)>1:
    command=sys.argv[1:]
else:
    command=input(":_ ").strip().strip("_").strip(".").split()
if len(command)>3:
    print("you input more than 3 inputs 'only 3 or less required'")
else:
    if command[0].lower() in instr:
        if len(command)==2:
            if command[1] in instr[command[0]]:
                instr[command[0]][command[1]]()
            else :
                instr[command[0]](command[1])
        elif command[1] in instr[command[0]]:
            instr[command[0]][command[1]](command[2])
        else:
            print("You didn't inout a valid command 'the second is wrong' ")
    else: 
        print("You didn't inout a valid command 'the first is wrong' ")