# This function will be tested automatically.
# Do not change the function name or parameters.
from functools import wraps

def cache_results(func):
    # Write your code below this line
    @wraps(func)
    def wrapperFunction(*args, **kwargs):
        lastResult = dict()
        result = int(args[0]) * int(args[1])

        if len(lastResult) != 0:
            if (args[0]==lastResult['firstArgument'] and args[1]==lastResult['secondArgument']):
                return (f"From Cache: {lastResult['result']}")
            else:
                lastResult['firstArgument'] = args[0]
                lastResult['secondArgument'] = args[1]
                lastResult['result'] = result
                return (f"Computed: {result}")
        else:
            lastResult['firstArgument'] = args[0]
            lastResult['secondArgument'] = args[1]
            lastResult['result'] = result
            return (f"Computed: {result}")
    return wrapperFunction


        



@cache_results
def multiply(a: int, b: int) -> int:
    return a * b

print(multiply(10, 20))
print(multiply(30, 40))
print(multiply(30, 40))