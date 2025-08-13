class Chai:
    masala = "Ginger"
    isHot = True

# Creating object
kesarChai = Chai()
# Modifying attributes in the object's namespace
kesarChai.masala = "Kesar"
print(f"Before Deleting - ")
print(f"Masala: {kesarChai.masala}, Hot Chai ? {kesarChai.isHot}")

# Deleting an attribute from object which exists in class
del kesarChai.masala 
print(f"\nAfter Deleting - ")
print(f"Masala: {kesarChai.masala}, Hot Chai ? {kesarChai.isHot}") 
# Falls back to Class's default value, Nothing to fall back in object, shadow
# will fall back to class itself 

# Deleting an attribute from object which doesn't exist in class
del kesarChai.taste # ERROR !!!