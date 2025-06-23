import os
from datetime import datetime
from datetime import date
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
            Data=json.load(f)
        except json.JSONDcodeError:
            Data=[]

else:
    Data=[]

Data.append(data)

with open(filename, "w") as f:
    json.dump(Data, f, indent=3)