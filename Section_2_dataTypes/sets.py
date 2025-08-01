cakeFlavors = {"Chocolate", "Vanilla", "Strawberry"}
iceCreamFlavors = {"Chocolate", "Vanilla", "Strawberry", "Butterscotch"}
# Union
allFlavors = cakeFlavors | iceCreamFlavors
print(f"All Flavors: {allFlavors}")
# Find common elements of 2 sets
commonFlavors = cakeFlavors & iceCreamFlavors
print(f"Common Flavors: {commonFlavors}")
# Flavors only in ice-cream
print(f"Flavors only in ice-cream: {iceCreamFlavors - cakeFlavors}")
# Membership testing
print(f"Is Cheese in cake flavors ? {'cheese' in cakeFlavors}")


# frozensets
# Create a frozenset
my_frozenset = frozenset([1, 2, 3])

# This will raise an error because frozensets are immutable
# my_frozenset.add(4) # Raises AttributeError

# Frozensets can be elements of a set
my_set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
print(my_set_of_sets)