def add_task(tasks, name_task):
    new_task = {"name": name_task, "completed": False}
    tasks.append(new_task)
    print(f"The task '{name_task}' was successfully added!")
    return

def view_tasks(tasks):
    print("Task List:")
    for index, task in enumerate(tasks, start=1):
      status = "✅" if task["completed"] else " "
      name_task = task["name"]
      print(f"{index}. [{status}] {name_task}")
    return

def update_task_name(tasks, index, name_task):
    adjust_index = int(index) -1
    if adjust_index >= 0 and adjust_index < len(tasks): 
      print(f"Task {index} updated to '{name_task}'")
      tasks[adjust_index]["name"] = name_task
    else:
      print("Invalid Index Tasks")
    return

def completed_task(tasks, index):
  adjust_index = int(index) -1
  tasks[adjust_index]["completed"] = True
  print(f"Task {index} check the completed")
  return 

def delete_tasks_completed(tasks):
  for task in tasks: 
    if task["completed"]:
      tasks.remove(task) 
  print("Completed task be deleted")   
  return 

tasks = []

while True:
    print("\nTask Manager Menu:")
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Update Tasks")
    print("4. Complete Tasks")
    print("5. Delete Completed Tasks")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
      name_task = input("Enter the name of the task you want to add: ")
      add_task(tasks, name_task)
    elif choice == "2":
      view_tasks(tasks)
    elif choice == "3":
      view_tasks(tasks)
      index_task = input("Enter the index of the task you want to update: ")
      name_task = input("Enter the new name of the task: ")
      update_task_name(tasks, index_task, name_task)
    elif choice == "4":
      view_tasks(tasks)
      index_task = input("Enter the index of the task you want to completed: ")
      completed_task(tasks, index_task)
    elif choice == "5":
      delete_tasks_completed(tasks)
    elif choice == "6":
        break

print("Program Terminated")
