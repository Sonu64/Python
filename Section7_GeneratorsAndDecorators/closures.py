# Global Var names to hold all parameters passed to printName
names = []
def printName(name):
    # names = [] Creates empty List everytime function is called, not containing anything
    # Accessing global variable
    names.append(name)
    print(f"{names}")
printName("Sonu") # Output: Sonu

# Modifying global vars outside function -> A Problem to overcome
names.append("Ooops ! Modified by mistake !")
printName("Shanu")

#_____________________________________________________________#

# Closures

def printWithMemory():
    names = []
    def innerFunction(name):
        names.append(name)
        print(f"{names}")
    return innerFunction

printNameWithMemory = printWithMemory() 
# Now this var holds innerFunction with access to names, names is created only once 
# during definition. names get attached to printWithMemory()
printNameWithMemory("Sonu") # These calls do not re-create the list names
printNameWithMemory("Manisha") 