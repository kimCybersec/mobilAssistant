import json
import time
import os
from datetime import datetime, timedelta
from plyer import notification
from kivy.clock import Clock

dataFile = "data/schedule.json"
weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def loadSchedule():
    if not os.path.exists(dataFile):
        with open(dataFile, "w") as f:
            json.dump({day: [] for day in weekDays}, f, indent=4)
    with open(dataFile, "r") as f:
        return json.load(f)
    
def parseTimeString(time_str):
    try:
        return datetime.strptime(time_str, "%H:%M").time()
    except ValueError:
        print(f"Invalid time format: {time_str}. Use HH:MM format.")
        return None
    
def sendNotification(task, message):
    notification.notify(
        title = "Task Reminder",
        message =  message,
        timeout = 10
    )
    
def reminderLoop():
    print("Reminder loop started...........press Ctrl+C to stop")
    while True:
        schedule = loadSchedule()
        today = datetime.now().strftime("%A")
        now = datetime.now().time()
        for task in schedule.get(today, []):
            if isinstance(task, dict) and "time" in task:
                taskTime = parseTimeString(task["time"])
                if taskTime and taskTime <= now:
                    sendNotification(f"Upcoming task: {task["title"]}", f"Start at {task["time"]}")
        
        time.sleep(60)
        
if __name__ == "__main__":    
    try:
        reminderLoop()
    except KeyboardInterrupt:
        print("Reminder service stopped by user.")
    