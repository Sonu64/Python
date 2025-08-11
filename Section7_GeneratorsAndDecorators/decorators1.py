def decoratorFunction(functionName):
    def wrappedFunction():
        print(f"Before calling {functionName.__name__}")
        functionName()
        print(f"After calling {functionName.__name__}")
    return wrappedFunction

# printHello() passed as param to decoratorFunction once we sprinkle it on top of printHello
@decoratorFunction
def printHello():
    print(f"Hello !")

printHello()