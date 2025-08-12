# A decorator in Python is simply a function that takes another function as input and 
# returns a new function that usually extends or modifies the behavior of the original 
# function — without actually changing its code.

# During definition - decoratorFunction is called, returning wrappedFunction as an object
# During call of decorated function - The returned wrappedFunction gets called, decoratorFunction
# doesn't gets called.

from functools import wraps

def decoratorFunction(functionName):
    @wraps(functionName) # Preserves the metadata about the passed function, nothing else
    # function definition to extend passed function
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

# Name and other metadata changes of the function we decorate
print(f"Function Name after passing it to decorator function: {printHello.__name__}")
# Output : wrappedFunction if @wraps is not used

