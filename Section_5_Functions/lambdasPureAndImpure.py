def pure_add(a, b):
    return (a + b)

counter = 0
def impure_increment():
    global counter
    counter += 1
    return counter

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def square_list(nums):
    newList = list(map(lambda num : num * num, nums))
    return newList
    
    
    