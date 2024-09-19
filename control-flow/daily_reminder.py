task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").lower().strip()
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()


match priority:
    case "high":
        if time_bound == 'yes':
            print()
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
    case "medium":
        print()
        print(f"Reminder: {task} is a {priority} priority task. Consider completing it when you have free time")
    case "low":
        print()
        print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
    case _:
        print()
        print("Invalid input. Please enter yes or no.")
print()








