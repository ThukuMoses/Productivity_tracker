import os
from datetime import datetime, date
import json


# Get today's date in ISO format (YYYY-MM-DD)
today=date.today().isoformat()

# Loop until valid wake-up time is entered (in HH:MM 24hr format)
while True:
    try:
        Wakeup_time=input("At what time did you wake up?(HH:MM) 24hr : ")
        wake_time=datetime.strptime(Wakeup_time, "%H:%M").time()# validate time format
        break
    except ValueError:
        print("Invalid time, Enter time in correct format!")

# Collect daily input from the user
number_of_tasks_completed=int(input("How many tasks did you complete?: "))
focus_rate=int(input("What was you focus rate?(1-10): "))
notes= input("Any thoughts about your day?: ")

filename="data.json"
# Create a dictionary for today's log
data= {
    "Date":today,
    "Wakeup_time":Wakeup_time,
    "Number_of_tasks_completed":number_of_tasks_completed,
    "Focus":focus_rate,
    "Notes/thoughts":notes,
}


# Load existing logs if the file exists, otherwise start with an empty list
if os.path.exists(filename):
    with open (filename, "r") as f:
    
        try:
            existing_logs=json.load(f)
        except json.JSONDecodeError:
            existing_logs=[] # If file is empty or corrupted, start fresh

else:
    existing_logs=[]


# Add today's log to the list
existing_logs.append(data)

# Save all logs back to the file
with open(filename, "w") as f:
    for i, log in enumerate(existing_logs):#addition of index to data dictionary
        log['index']=i   
    json.dump(existing_logs, f, indent=3)

    for log in existing_logs:
        print(f"\n\nDate: {log['Date']}\nWake_time: {log['Wakeup_time']}\nTasks completed: {log['Number_of_tasks_completed']}\nFocus: {log['Focus']}\nNotes/Thoughts: {log['Notes/thoughts']}\n\n")
        print("-"*40)#for visual clarity

    log_count=0
    
    for log in existing_logs:
        log_count+=1 # count number of logs
    total_focus=sum(log["Focus"] for log in existing_logs)
    total_tasks=sum(log["Number_of_tasks_completed"]for log in existing_logs)
        # Print out summary metrics
    print(f"Total tasks: {total_tasks} | Number of logs: {log_count} | Total focus: {total_focus}")
    # Function to calculate average focus
    def average():
        return total_focus/log_count if log_count >0 else 0#condition to avoid division by zero error
    print(f"Average focus:{average()}")

    max_tasks=max(log["Number_of_tasks_completed"] for log in existing_logs)
    max_focus=max(log["Focus"]for log in existing_logs)
    def productive_day():
        return[f'On {log["Date"]}, you completed {log["Number_of_tasks_completed"]} tasks with focus of {log["Focus"]}'
         for log in existing_logs
         if log["Number_of_tasks_completed"]==max_tasks and log["Focus"]==max_focus]
        
    #print(data)


for message in productive_day():
    print(message)
