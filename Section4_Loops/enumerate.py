# This function will be tested automatically. 
# Do not change the function name or parameters.
def generate_numbered_tasks(tasks: list[str]) -> list[str]:
	finalList = []
	for index, task in enumerate(tasks, start=1):
		finalList.append(f"{index}. {task}")
	return finalList

	
print(generate_numbered_tasks(["Football practice", "Python course"]))