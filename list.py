task = []

print("====== TO DO LIST =====")
print("1. Add task")
print("2. View task")
print("3. Remove task")
print("4. Exit")

choice = input("choose your option: ")
if choice == "1":
    task = input("Enter a task: ")
task.append({"name": task, "completed" : False})
print("task added successfully")



