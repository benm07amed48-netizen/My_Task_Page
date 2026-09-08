from datetime import datetime , timedelta , date
import json


speech="Since it's your first time chack the 'README' file for the best experience instructions . "

speech1= """
==================================================
                   INSTRUCTIONS
==================================================
  l all         -> Show full task list
  l todo        -> Show pending tasks (To-Do)
  l done        -> Show completed tasks
  a <title>     -> Add a new task
  d <id>        -> Delete a task
  i <id>        -> Show task details
  e info <id>   -> Edit task details
  e stat <id>   -> Change task status
==================================================
"""

speech2="""
==================================================
Enter field number [1-6] and new value in quotes ("..."):
Example usage: 1 "LOW"  or  5 "2h"

[1] Priority     -> 3-letter tag (LOW, MED, MAX, URG)
[2] Description  -> Text description
[3] CreatedAt    -> Date format (MM/DD)
[4] Deadline     -> Date format (MM/DD)
[5] Est. Time    -> Time duration (e.g., 30m, 2h)
[6] UpdatedAt    -> Date format (MM/DD)
[0] Cancel       -> Cancel the editing
==================================================
Choice: """


def new_user():
    try:
        with open("tasks.json","x") as f:
            print(speech)
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
        print(speech1)


def load_tasks():
    with open("tasks.json","r") as l:
        return json.load(l)

    
def save_taks(a):
    with open("tasks.json","w") as l:
        json.dump(a,l,indent=4,sort_keys=True)     
    return "saving succesfull"


def id_check(id):
   if id.lower().strip().strip("\#").strip() in load_tasks() : return False
   else : return True




def l_all():
    list=load_tasks()
    print("-----| full list:")
    for id in list:
        print(f"●[#{id}] • [{list[id][0]}] • [{list[id][1]}] • {list[id][2]}\n")


def l_todo():
    list=load_tasks()
    print("-----| todo list:")
    for id in list:
        if list[id][0]=="Done": continue
        print(f"●[#{id}] • [{list[id][0]}] • [{list[id][1]}] • {list[id][2]}\n")


def l_done():
    list=load_tasks()
    print("-----| done list:")
    for id in list:
        if list[id][0]=="Todo": continue
        print(f"●[#{id}] • [{list[id][0]}] • [{list[id][1]}] • {list[id][2]}\n")


def info(id):
    if id_check():print("wrong id ... canceling .");return
    list=load_tasks()
    print(f"-----| Task: \n[#{id}] [{list[id][0]}] [{list[id][1]}] {list[id][2]}\n           └─ Created: {list[id][3]} | Deadline: {list[id][4]} | Est.t: {list[id][5]} | {"Updated" if list[id][0] !="Done" else "Finished"}: {list[id][6]}\n")


def d_del(id):
    if id_check():print("wrong id ... canceling .");return
    list=load_tasks()
    print(f"-----| The Task going to be deleted: \n[#{id}] [{list[id][0]}] [{list[id][1]}] {list[id][2]}\n           └─ Created: {list[id][3]} | Deadline: {list[id][4]} | Est.t: {list[id][5]} | {"Updated" if list[id][0] !="Done" else "Finished"}: {list[id][6]}\n")
    ans=input("type Yes<-- [Y/N] -->No:\n\\").strip().lower()[0]
    if ans=="y":
        list.pop(id)
        print("The task has been deleted")  
        print(save_taks(list))


def e_stat(id):
    if id_check():print("wrong id ... canceling .");return
    list=load_tasks()
    print(f"-----| The Task going to set as '{"Done" if list[id][0]=="Todo" else "Todo"}': \n[#{id}] [{list[id][0]}] [{list[id][1]}] {list[id][2]}\n           └─ Created: {list[id][3]} | Deadline: {list[id][4]} | Est.t: {list[id][5]} | {"Updated" if list[id][0] !="Done" else "Finished"}: {list[id][6]}\n")
    ans=input("type Yes<-- [Y/N] -->No:\n\\").strip().lower()[0]
    if ans=="y":
        list[id][0]= "Done" if list[id][0]=="Todo" else "Todo"
        list[id][6]=date.today().strftime("%m/%d")
        print(f"The task is being set to '{list[id][0]}'")
        print(save_taks(list))

def parsing(txt):
    try:
        rslt=txt.index(" ")
    except ValueError:
        txt=txt.replace('"'," ",1)
    if speech.startswith("0") : print("... canceling\nCanceled");return False
    rslt=txt.strip(".").strip().split(maxsplit=1)
    if len(rslt)!= 2:
        print("you didn't input the new value\n... editing canceled.try again")
        return False
    rslt[0]=int(rslt[0].strip().strip('"'))
    rslt[1]=rslt[1].strip('"').capitalize()+(" ." if rslt[0]==2 else "")
    if rslt[0]==1 :rslt[1]=rslt[1].upper()
    if rslt[0] not in range(1,7):
        print(f"the command is wrong {rslt[0]} is out of range\n... editing canceled.try again")
        return False
    return rslt


def e_info(id):
    if id_check():print("wrong id ... canceling .");return
    list=load_tasks()
    print(f"-----| The Task going to be edited : \n[#{id}] [{list[id][0]}] [{list[id][1]}] {list[id][2]}\n           └─ Created: {list[id][3]} | Deadline: {list[id][4]} | Est.t: {list[id][5]} | {"Updated" if list[id][0] !="Done" else "Finished"}: {list[id][6]}\n")   
    ans=input(speech2)
    ans=parsing(ans.strip())
    if ans:
        list[id][ans[0]]= ans[1]
        list[id][6]=date.today().strftime("%m/%d")
        print("... editing in progress ")
        print(save_taks(list))
    else:return


def id_create(*key):

    if key[0]=="URG": one ="a"
    elif key[0]=="MAX": one="i"
    elif key[0]=="MED": one="r"
    elif key[0]=="LOW": one="x"
    else : one="z"
    two=key[1][1]+key[1][-1]
    three=key[2].strip()[0].lower()+key[2][key[2].strip().find(" ")+1].lower()
    four=datetime.now().microsecond[-3:]
    return one+two+three+four


def a_add(txt):
    list=load_tasks()
    elements={}

    print(f"●The title of the new task: [{txt.strip().capitalize()+" ."}]")
    ans=input("Enter nex task description or No/N to keep the current task title: ").strip().strip('"').lower()
    elements["desc"]=txt if ans=="no" or ans=="n" else ans.capitalize()+" ."

    ans=input("Enter priority [LOW / MED / MAX / URG]: ").strip().upper()[:3]
    elements["priority"]=ans if ans in ["LOW","MED","MAX","URG"] else "MED"

    ans=input("Enter deadline [MM/DD] (Press Enter to skip): ").strip()
    elements["deadline"]=ans if ans.find("/")!=-1 else "N/A"

    ans=input("Enter estimated time (e.g., 30m, 2h, daily) (Default: 0m): ").strip()
    elements["est"]="0m" if ans.isspace() or not ans else ans

    elements["stat"]="Todo"
    elements["create"],elements["update"]=date.today().strftime("%m/%d")
    elements["id"]=id_create(elements["priority"],elements["create"],elements["desc"])

    list[elements["id"]][0]=elements["stat"]
    list[elements["id"]][1]=elements["priority"]
    list[elements["id"]][2]=elements["desc"]
    list[elements["id"]][3]=elements["create"]
    list[elements["id"]][4]=elements["deadline"]
    list[elements["id"]][5]=elements["est"]
    list[elements["id"]][6]=elements["update"]
    print("... saving in progress")
    print(save_taks())
    return
    