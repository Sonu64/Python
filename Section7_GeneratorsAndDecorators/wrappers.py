def f1(functionName):
    def wrapper():
        print("Before...")
        functionName()
        print("After...")
    return wrapper

def sampleFunction():
    print("Hello !")

modifiedSampleFunction = f1(sampleFunction)
modifiedSampleFunction()