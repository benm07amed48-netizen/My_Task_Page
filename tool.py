from datetime import datetime , timedelta

def new_user():
    try:
        with open("tasks.json","x") as f:
            print("Since it's your first time chack the 'README' file for the best experience instructions . ")
    except FileExistsError:
        pass

def logs():
    with open("log.txt","+a") as log:
        log.write("\n"+str(datetime.now()))

def instruction(maxdel=timedelta(minutes=1)):
    with open("log.txt","a+") as log:
        log.seek(log.tell()-26)
        last=datetime.strptime(log.read(),"%Y-%m-%d %H:%M:%S.%f")
    diff = datetime.now() - last
    if diff >= maxdel :
        print("="*60+"""
                Instruction :
    _ l: show full task List.
    _ l todo: show task List TO be DOne.
    _ l done: show task List DONE.
    _ e info: Edit task INFO.
    _ e stat: Edit task STAT.
    _ a : Add new task.
    _ d <task id>: Delete task with the id '<task id>'.
    _ i <task id>: show task'<task id>' Info.
"""+"="*60)

def act():
    if command[0].lower() in instr:
    if len(command)==2 and command[1].lower()in instr[command[0]]:
        tool.act()
    else:
        tool.act()