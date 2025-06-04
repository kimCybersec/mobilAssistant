import json
import os

dataFile = "data/schedule.json"
weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def checkSchedule():
    if not os.path.exists(dataFile):
        with open(dataFile, "w") as f:
            json.dump({day: [] for day in weekDays}, f, indent = 4)
            
def loadSchedule():
    checkSchedule() 
    with open(dataFile, "r") as f:
        return json.load(f)
    
def saveSchedule(schedule):
    with open(dataFile, "w")as f:
        json.dump(schedule, f, indent = 4)
        
def markDone(day, taskTitle):
    schedule = loadSchedule()
    for task in schedule.get(day, []):
        if isinstance(task, dict) and task.get("title") == taskTitle:
            task["status"] = "done"
            
        elif isinstance(task, str) and task == taskTitle:
            idx = schedule[day].index(task)
            schedule[day][idx] = {"title": task, "status": "done"}
    saveSchedule(schedule)
    
def showSummary():
    schedule = loadSchedule()
    total = "done" = 0   
    for day in weekDays():
        for task in schedule[day]:
            if isinstance(task, dict):
                total += 1
                if task.get("status") == "done":
                    done += 1
                status = task.get("status", "pending")
            elif isinstance(task, str):
                total += 1
                
    print(f"Total tasks: {total}, Done: {done}, Pending: {total - done}")
    
def showAllTasks():
    schedule = loadSchedule()
    for day in weekDays:
        print(f"\n {day}:")
        for task in schedule.get(day, []):
            if isinstance(task, dict):
                status = task.get("status", "pending")
                print(f"  - {task['title']} [{status}]")
            elif isinstance(task, str):
                print(f"  - {task} [pending]")
        print() 
  
if __name__ == "__main__":
    showAllTasks()
    showSummary()
    markDone("Monday", "Task 1")      