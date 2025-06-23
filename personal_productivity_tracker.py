import os
from datetime import datetime, date
import json

today=date.today().isoformat()
while True:
    try:
        Wakeup_time=input("At what time did you wake up?(HH:MM) 24hr : ")
        wake_time=datetime.strptime(Wakeup_time, "%H:%M").time()
        break
    except ValueError:
        print("Invalid time, Enter time in correct format!")

Number_of_tasks_completed=int(input("How many tasks did you complete?: "))
Focus_rate=int(input("What was you focus rate?(1-10): "))
notes= input("Any thoughts about your day?: ")

filename="data.json"

data= {
    "Date":today,
    "Wakeup_time":Wakeup_time,
    "Number_of_tasks_completed":Number_of_tasks_completed,
    "Focus":Focus_rate,
    "Notes/thoughts":notes,
}

if os.path.exists(filename):
    with open (filename, "r") as f:
    
        try:
            existing_logs=json.load(f)
        except json.JSONDecodeError:
            existing_logs=[]

else:
    existing_logs=[]

existing_logs.append(data)

with open(filename, "w") as f:
    json.dump(existing_logs, f, indent=3)

with open(filename, "r") as f:
    existing_logs=json.load(f)
    for log in existing_logs:
        print(f"\n\n\nDate: {log['Date']}\nWake_time: {log['Wakeup_time']}\nTasks completed: {log['Number_of_tasks_completed']}\nFocus: {log['Focus']}\nNotes/Thoughts: {log['Notes/thoughts']}")

