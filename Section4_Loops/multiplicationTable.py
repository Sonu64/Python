# This function will be tested automatically. 
# Do not change the function name or parameter type.
def multiplication_table(number: int) -> list[str]:
    # Write your code below this line
    table = []
    for i in range(1, 11):
        table.append(f"{number} x {i}  = {(number * i)}")
    return table
    pass

print(multiplication_table(7))