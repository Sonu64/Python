# Python is dynamically typed, that means data type gets automatically decided by the compiler
# once we create a variable.
# Learn about Integers, Reals(Floating points) from notes


# Decimals and Fractions
from decimal import Decimal
price = Decimal('19.99')
tax_rate = Decimal('0.07')
large_value = Decimal('0.99999999999999999999999')
largeValueWithoutDecimalFunction = 0.999999999999999999999999999
total = price * (1 + tax_rate)
print(f"Decimal Total: {total}")
print(large_value) # Exact printed
print(largeValueWithoutDecimalFunction) # Rounded off to 1

from fractions import Fraction
f1 = Fraction(3, 4)
f2 = Fraction(1, 2)
sum_fractions = f1 + f2
print(f"Fraction Sum: {sum_fractions}") # 5/4




# Booleans
is_active = True
has_permission = False
print(f"Am I active: {is_active}")
print(f"Permission granted ? {has_permission}")
print(f"{bool(190)}") # True, any non-zero value is True
print(f"{bool(None)}") # False
# Logical Operators
print(f"Can I enter the room ? {is_active and has_permission}") # False
print(f"Is it true that I don't have permission ? {not has_permission}") # True
print(f"Am I active or do I have permission ? {is_active or has_permission}") # True



# Complex Numbers
c1 = 2 + 3j
c2 = 1 - 2j
sum_complex = c1 + c2
product_complex = c1 * c2
print(f"Complex Sum: {sum_complex}")
print(f"Complex Product: {product_complex}")