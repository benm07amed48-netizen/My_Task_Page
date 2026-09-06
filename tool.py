from datetime import datetime , timedelta
import json

def new_user():
    try:
        with open("tasks.json","x") as f:
            print("Since it's your first time chack the 'README' file for the best experience instructions . ")
    except FileExistsError:
        pass

def logs():
    with open("log.txt","+a") as log:
        log.write("\n"+str(datetime.now()))

def instruction(maxdel=timedelta(minutes=1.5)):
    with open("log.txt","a+") as log:
        log.seek(log.tell()-26)
        last=datetime.strptime(log.read(),"%Y-%m-%d %H:%M:%S.%f")
    diff = datetime.now() - last
    if diff >= maxdel :
        print("="*50+"""
                        Instruction :
    _ l all:--------show Full task List.
    _ l todo:-------show task List TO be DOne.
    _ l done:-------show task List DONE.
    _ a <title>:----Add new task.
    _ d <id>:-------Delete task.
    _ i <id>:-------show task details.
    _ e info <id>:--Edit task INFO.
    _ e stat <id>:--change task STAT.
"""+"="*50)

def l_all():
    with open("tasks.json","r") as l:
        list=json.load(l)
    print("-----| full list:")
    for id in list:
        print(f"●[#{id}] • [{list[id][0]}] • [{list[id][1]}] • {list[id][2]}\n")

def l_todo():
    with open("tasks.json","r") as l:
        list=json.load(l)
    print("-----| todo list:")
    for id in list:
        if list[id][0]=="Done": continue
        print(f"●[#{id}] • [{list[id][0]}] • [{list[id][1]}] • {list[id][2]}\n")

def l_done():
    with open("tasks.json","r") as l:
        list=json.load(l)
    print("-----| done list:")
    for id in list:
        if list[id][0]=="Todo": continue
        print(f"●[#{id}] • [{list[id][0]}] • [{list[id][1]}] • {list[id][2]}\n")

#    └─ Created: {list[id][3]} | Deadline: {list[id][4]} | Est.t: {list[id][5]} | {"Updated" if list[id][0] !="Done" else "Finished"}: {list[id][6]}\n
