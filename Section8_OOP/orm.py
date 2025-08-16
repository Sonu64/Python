# According to Method Resolution Order (MRO), the class that is being inherited first
# will get the priority.

class A:
    label = "A: Base Class"

class B(A):
    label = "B: Class B"

class C(A):
    label = "C: Class C"

class D(B, C):
    pass

cup = D() # OUTPUT: B: Class B
print(cup.label)
print(D.__mro__)