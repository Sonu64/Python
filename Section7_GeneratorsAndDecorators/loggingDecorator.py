from functools import wraps

def loggerFunction(passedFunction):
    # Step 1: Preserve metadata about passed function
    @wraps(passedFunction)
    # Step 2: Define wrapperFunction
    def wrapperFunction(*args, **kwargs):
        print(f"\nBefore calling {passedFunction.__name__} with Args {args} and Kwargs {kwargs}")
        passedFunction(*args, **kwargs)
        print(f"After calling {passedFunction.__name__} with Args {args} and Kwargs {kwargs}")
    return wrapperFunction

@loggerFunction
# Step 3: Define the function
def ingredients(mainIngredient1, mainIngredient2, sweetener = "Sugar"):
    print(f"Main Ingredients are {mainIngredient1}, {mainIngredient2}, Sweetener is {sweetener}")

@loggerFunction
# Define another function
def printAges(sonu, ma, baba):
    print(f"Age of Sonu is {sonu} years, that of Ma is {ma} years and that of Baba is {baba} years")

# Step 4: Call the functions

# Args and kwargs both used, Honey overwriting default sweetner Sugar
ingredients("Coffee Beans", "Cocoa Powder", sweetener="Honey")
# All parameters passed as kwargs
printAges(sonu=22, ma=42, baba=48)
# All parameters passed as positional args
printAges(26, 48, 52)