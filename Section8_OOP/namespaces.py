class Chai:
    origin = "India"

# Accessing directly from class
print(Chai.origin)
# Adding more Class variables from outside
Chai.masala = "Kesar"
# Printing class variable masala
print(Chai.masala)

# Creating objects
gingerTea = Chai()
gingerTea.origin = "North India"
gingerTea.masala = "Ginger"
# Printing Object variables, demonstrating that each object has its own namespace
# which doesn't affect the main class defined vars if they are changed in the object entities
print("Class Variables:")
print(f"Origin: {Chai.origin}")
print(f"Masala: {Chai.masala}")
print("\nObject variables: ")
print(f"Origin: {gingerTea.origin}")
print(f"Masala: {gingerTea.masala}")

# Adding more properties to object
gingerTea.taste = "Awesome" # This property doesn't exist in class
print(gingerTea.taste)

