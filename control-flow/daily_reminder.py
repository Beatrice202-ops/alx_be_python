# task_variable = input("enter your task: ")
# task_priority = input("Priority (high/medium/low): ")
# time_bound = input("Is it time-bound? (yes/no):")

# match task_priority:
#     case "high":
#         reminder = f"{task_variable}, is a high priority task that requires immediate attention today!"
#     case "medium":
#         reminder = f"{task_variable}, is a medium priority task that requires less attention today!"
#     case "low":
#         reminder = f"{task_variable}, is a low priority task that requires lowe attention today!"
# if time_bound == "yes":
#     reminder += "this task is time bound"
# else:
#     reminder += "this task is not time bound"
# print(reminder)

#!/usr/bin/env python3

# daily_reminder.py

# --- Input section ---
task = input("Enter the task description: ").strip()

# Validate priority with a loop (no data structures to store multiple tasks)
priority = input("Set the task priority (high/medium/low): ").strip().lower()
while priority not in ("high", "medium", "low"):
    print("Please enter one of: high, medium, low.")
    priority = input("Set the task priority (high/medium/low): ").strip().lower()

time_bound = input("Is the task time-bound? (yes/no): ").strip().lower()
while time_bound not in ("yes", "no"):
    print("Please answer yes or no.")
    time_bound = input("Is the task time-bound? (yes/no): ").strip().lower()

# --- Processing / control flow ---
# Match Case requires Python 3.10+
match priority:
    case "high":
        reminder = f"{task}, is a high priority task that requires immediate attention today!"
    case "medium":
        reminder = f"{task}, is a medium priority task that requires less attention today!"
    case "low":
        reminder = f"{task}, is a low priority task. Consider completing it when you have free time."
    case _:
        # Shouldn't happen because we validated, but keep a safe fallback
        reminder = f"Task: {task} (unknown priority: {priority})."

# Time-sensitivity tweak
if time_bound == "yes":
    reminder += " This task is time-bound "
else:
    reminder += " This task is not time-bound"

# --- Output ---
print(f"Reminder: {reminder}")

