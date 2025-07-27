task_variable = input("enter your task: ")
task_priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no):")

match task_priority:
    case "high":
        reminder = f"{task_variable}, is a high priority task that requires immediate attention today!"
    case "medium":
        reminder = f"{task_variable}, is a medium priority task that requires less attention today!"
    case "low":
        reminder = f"{task_variable}, is a low priority task that requires lowe attention today!"
if time_bound == "yes":
    reminder += "this task is time bound"
else:
    reminder += "this task is not time bound"
print(reminder)

