import os

print("Tashwill's Task Automator 2026")
print("-" *40)

filename = "task_log.txt"

task_input=input("Enter your task to automate ")

if task_input.strip() == "":
    print("Error: Task cannot be empty.")
else:
    with open(filename, "a") as file:
        file.write(f"-{task_input}\n")

    print(f"Success! Task is logged to '{filename}'.")
print("-" *40)

print("Current Automated Tasks Queue:")
if os.path.exists(filename):
    with open(filename, "r") as file:
        print(file.read())
else:
    print("Queue is empty>")


