import json
data=[
    {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
    {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
    {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
]
with open("tasks.json",'w') as f:
    json.dump(data,f)
with open("tasks.json",'r') as f:
    jsondata = json.load(f)
    print(f'ID   Task    Completed    Priority')
    for task in jsondata:
        print(f"{task['id']} {task['task']}  {task['completed']}  Priority: {task['priority']}")
# functions to display:
def totaltasks():
    total=0
    for task in jsondata:
        total += 1
    return total

def completedtasks():
    total=0
    for task in jsondata:
        if task['completed']:
            total += 1
    return total

def pendingtasks():
    total=0
    for task in jsondata:
        if task['completed']==False:
            total += 1
    return total

def Avaraggepriority():
    total=0
    counter=0
    for task in jsondata:
        total+=task['priority']
        counter+=1
    return total/counter


print(f'Total tasks: {totaltasks()}, Completed tasks: {completedtasks()}, Pending tasks: {pendingtasks()}, Avaraggepriority: {Avaraggepriority()}')
# Converting
with open("tasks.json",'r') as f:
    jsondata = json.load(f)

    with open("tasks.csv",'w') as file:
        writer = csv.DictWriter(file,fieldnames=jsondata[0].keys())
        writer.writeheader()
        for task in jsondata:
            writer.writerow(task)
