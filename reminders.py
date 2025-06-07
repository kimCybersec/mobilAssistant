from plyer import notification
from datetime import datetime
from kivy.clock import Clock
import json
import os

DATA_FILE = "data/schedule.json"
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def loadSchedule():
    if not os.path.exists(DATA_FILE):
        return {day: [] for day in WEEKDAYS}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def sendNotification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=5
    )

def checkTasks(dt):
    now = datetime.now()
    today = now.strftime("%A")
    current_time = now.strftime("%H:%M")

    schedule = loadSchedule()
    for task in schedule.get(today, []):
        if isinstance(task, dict) and task.get("time") == current_time:
            sendNotification(f"Reminder: {task['title']}", f"Scheduled for {task['time']}")

def startReminders():
    Clock.schedule_interval(checkTasks, 60)  # every 60 seconds
