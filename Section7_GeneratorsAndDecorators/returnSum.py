from functools import wraps

def decoratorFunction(functionName):
    @wraps(functionName)
    def wrapperFunction(*args, **kwargs):
        print(f"\nBefore calling {functionName.__name__}")
        print(f"Args: {args}, Kwargs: {kwargs}")
        result = functionName(*args, **kwargs)
        print(f"After calling {functionName.__name__}")
        return result
    return wrapperFunction

@decoratorFunction
def sum(a, b, name="Guest"):
    return f"{a+b}, Name is {name}"

print(sum(10, 20))
print(sum(1, b=2, name='Sonu'))
