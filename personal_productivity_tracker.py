import os
import json
from datetime import datetime, date

class ProductivityTracker:
    def __init__(self):
        self.filename = "data.json"
        self.existing_logs = self.load_logs()

    def load_logs(self):
        """
        Load the logs from the JSON file, or return an empty list
        if the file does not exist or is corrupted.
        """
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                try:
                    logs = json.load(f)
                except json.JSONDecodeError:
                    logs = []
        else:
            logs = []
        return logs

    def save_logs(self):
        """
        Save the current state of existing_logs to the JSON file.
        """
        with open(self.filename, "w") as f:
            json.dump(self.existing_logs, f, indent=3)
        print("Logs saved successfully!")

    def collect_log_data(self, today: str)-> dict:
        """
        Prompt user to add a new productivity log and save it.
        """
        while True:
            try:
                wakeup_time = input("At what time did you wake up? (HH:MM 24hr): ")
                # validate format
                _ = datetime.strptime(wakeup_time, "%H:%M").time()
                break
            except ValueError:
                    print("Invalid time. Enter time in correct format (HH:MM)")

        number_of_tasks_completed = int(input("How many tasks did you complete?: "))
        focus_rate = int(input("What was your focus rate? (1-10): "))
        notes = input("Any thoughts about your day?: ")

        data = {
                "Date": today,
                "Wakeup_time": wakeup_time,
                "Number_of_tasks_completed": number_of_tasks_completed,
                "Focus": focus_rate,
                "Notes/thoughts": notes,
            }
        return data
    
    def add_log(self):
        today=date.today().isoformat()
        check_log=any((log["Date"])==today for log in self.existing_logs)
        if not check_log:
            data=self.collect_log_data(today)#call helper method
            self.existing_logs.append(data)
            self.save_logs()
        else:
            your_choice=input("""
                You already logged today
                1.Modify today's log
                2.quit
            Choose: """)
            match your_choice:
                case "1":
                    #rewrite existing logs without today's date
                    self.existing_logs=[log for log in self.existing_logs if log["Date"]!= today]
                    data=self.collect_log_data(today)
                    self.existing_logs.append(data)
                    self.save_logs()
                case "2":
                     print("Quitting without changes")   
                case _:
                    print("Invalid option! Please choose 1 or 2.")            


    def view_logs(self):
        """
        Returns all logs as a single formatted string.
        """
        log_strings = []
        for log in self.existing_logs:
            separator = "-" * 40
            details = (
                f"\nDate: {log['Date']}\n"
                f"Wakeup time: {log['Wakeup_time']}\n"
                f"Tasks completed: {log['Number_of_tasks_completed']}\n"
                f"Focus: {log['Focus']}\n"
                f"Notes/Thoughts: {log['Notes/thoughts']}\n"
            )
            formatted_string = separator + details
            log_strings.append(formatted_string)
        return "\n".join(log_strings)

    def average_focus(self):
        """
        Calculates and prints the average focus across all logs,
        along with total tasks and total focus.
        """
        if not self.existing_logs:
            print("Logs missing! Please check your data.json.")
            return

        log_count = len(self.existing_logs)
        total_focus = sum(log["Focus"] for log in self.existing_logs)
        total_tasks = sum(log["Number_of_tasks_completed"] for log in self.existing_logs)
        average = total_focus / log_count if log_count > 0 else 0

        print(f"Total tasks: {total_tasks} | Number of logs: {log_count} | Total focus: {total_focus}")
        print(f"Average focus: {average:.2f}")

    def most_productive_day(self) -> list[str]:
        """
        Identifies the most productive day(s) based on:
          - the highest number of tasks completed
          - and if tied, the highest focus among those days.
        Returns:
            A list of descriptive strings summarizing the most productive day(s).
            Returns an empty list if no logs exist.
        """
        if not self.existing_logs:
            print("Logs missing! Please check your data.json.")
            return []

        # highest task count across all logs
        max_tasks = max(log["Number_of_tasks_completed"] for log in self.existing_logs)

        # filter logs with the maximum tasks
        productive_logs = [
            log for log in self.existing_logs
            if log["Number_of_tasks_completed"] == max_tasks
        ]

        # among the productive_logs, find highest focus
        max_focus = max(log["Focus"] for log in productive_logs)

        if len(productive_logs) == 1:
            log = productive_logs[0]
            return [self.format_productive_log(log)]
        else:
            return [
                self.format_productive_log(log)
                for log in productive_logs
                if log["Focus"] == max_focus
            ]

    def format_productive_log(self, log: dict) -> str:
        """
        Helper method to return a human-readable summary of a single log.
        """
        return (
            f"On {log['Date']}, you completed {log['Number_of_tasks_completed']} tasks "
            f"with a focus score of {log['Focus']}."
        )
    
tracker = ProductivityTracker()

def test():
    if __name__ == "__main__":
        
        # Uncomment this to add a new log interactively
        tracker.add_log()
        
        # View all logs
        print("\n=== Viewing All Logs ===")
        print(tracker.view_logs())
        
        # Average focus and summary
        print("\n=== Average Focus ===")
        tracker.average_focus()
        
        # Most productive day
        print("\n=== Most Productive Day(s) ===")
        messages = tracker.most_productive_day()
        for m in messages:
            print(m)
#test()
#Menu for choosing the action to do
while True:
    choice=input("""
        1.Make tests
        2.Add log
        3.View logs
        4.Average focus
        5.Most productive day
        6.Quit
    Choose: """)

    match choice:
        case "1":
            test()
        case "2":
            tracker.add_log()
        case "3":
            print("\n=== Viewing All Logs ===")
            print(tracker.view_logs())
        case "4":
            print("\n=== Average Focus ===")
            tracker.average_focus()   
        case "5":
            message=tracker.most_productive_day()
            for m in message:
                print(m)
        case "6":
            break
        case _:
            print("Invalid option, try again.")
