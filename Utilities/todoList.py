import os
TEXT_FILE = "tasks.txt"

# Read all tasks
def loadTasks():
    tasks = []
    if (os.path.exists(TEXT_FILE)):
        with open(TEXT_FILE, "r", encoding="utf-8") as f:
            for line in f:
                taskName, status = line.strip().rsplit("||", 1)
                # Split from the right maximum ONCE, no issues if todo name has ||
                tasks.append({"taskName":taskName, "status":status})
    return tasks



# Save tasks in file
def saveTasks(tasks):
    with open(TEXT_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            taskName = task['taskName']
            if task['status'] == "done":
                status = "done"
            else:
                status = "not_done"
            f.write(f"Task: {taskName} || Status: {status}")






# Display all tasks
def displayTasks(tasks):
    if not tasks:
        print(f"No Tasks found !")
    else:
        for i, task in enumerate(tasks, 1):
            if task['status'] == 'done':
                checkbox = "✅"
            else:
                checkbox = " "
            print(f"{i}. [ {checkbox} ] {task['taskName']}")
    print()





# Managing the main Loop
def manageTasks():
    tasks = loadTasks()

    while True:
        print("\n---------- Task Manager ----------")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit App")

        choice = int(input("Choose option [1-5]: ").strip())

        match choice:
            case 1:
                taskName = input("Task name: ").strip()
                if taskName:
                    tasks.append({'taskName':taskName, 'status':"not_done"})
                    saveTasks(tasks)
                    print("Successfully Added task !")
                else:
                    print("Task can't be empty !")
            
            case 2:
                displayTasks(tasks)

            case 3:
                displayTasks(tasks)
                try:
                    completedTaskNumber = int(input("Enter Serial number of completed task: "))
                    if 1 <= completedTaskNumber <= len(tasks):
                        tasks[completedTaskNumber-1]['status'] = "done"
                        saveTasks(tasks)
                        print("Successfully Marked task as Done !")
                    else:
                        print("Invalid Serial Number !")
                except:
                    print("Invalid Input ! Please enter a number !")
                
            case 4:
                displayTasks(tasks)
                try:
                    deleteTaskNumber = int(input("Enter Serial number of task to delete: "))
                    if 1 <= deleteTaskNumber <= len(tasks):
                        del(tasks[deleteTaskNumber-1])
                        saveTasks(tasks)
                        print("Successfully Deleted Task !")
                    else:
                        print("Invalid Serial Number !")
                except:
                    print("Invalid Input ! Please enter a number !")

            case 5:
                print("Exiting App...")
                break;
                
            case _:
                print("Please enter valid option !")



manageTasks()