# This function will be tested automatically. 
# Do not change the function name or parameters.
def mark_completed_tasks(tasks: list[str]) -> list[str]:
    # Write your code below this line
    updatedList = []
    for task in tasks:
        updatedList.append(f"Completed: {task}")
    return updatedList
    pass