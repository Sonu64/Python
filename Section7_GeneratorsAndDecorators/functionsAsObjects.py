def f1():
    print("Inside f1")

def f2(functionName):
    print("Calling the function passed as parameter...")
    functionName()

functionObject = f1
f2(functionObject)