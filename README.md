# Productivity Tracker CLI

This is a simple command-line based productivity tracker built with Python. It helps you keep daily logs of your wake-up time, tasks completed, focus rating, and thoughts about your day. It then analyzes the data to show your average focus and the most productive days.

## Features
- Add a daily productivity log
- Prevent duplicate logs for the same day (with option to update)
- View all logs in a readable format
- See average focus across all days
- Identify your most productive day(s)

## How It Works

- Data is stored in a local `data.json` file.
- Each time you add a new log, the program checks whether you already logged for today, and allows you to modify it instead of duplicating.
- You can view logs, calculate averages, and get a productivity summary directly from the CLI menu.

## Usage

1. Clone this repository or download the files.
2. Make sure you have Python 3 installed.
3. In your terminal, run:
   ```bash
   python personal_productivity_tracker.py
