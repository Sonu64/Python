# Creating classes
class Vehicle:
    pass

class Student:
    pass

print(f"{type(Vehicle)}")

# Creating Objects
rickshaw = Vehicle()
print(type(rickshaw))

print(type(rickshaw) is Vehicle)
print(type(rickshaw) is Student)