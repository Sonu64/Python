my_tuple = (1, 2, 3)
print(f"Original Tuple: {my_tuple}, ID: {id(my_tuple)}")

# Trying to "change" a tuple actually creates a new one
my_tuple = my_tuple + (4,) # This creates a NEW tuple object
print(f"Modified Tuple: {my_tuple}, ID: {id(my_tuple)}")




my_list = [1, 2, 3]
print(f"Original List: {my_list}, ID: {id(my_list)}")

# Appending modifies the list IN-PLACE
my_list.append(4)
print(f"Modified List: {my_list}, ID: {id(my_list)}")






x = 5
print(f"x value: {x}, ID: {id(x)}")
x = 6 # x now refers to a NEW integer object
print(f"x value: {x}, ID: {id(x)}") # ID of the variable itself changes - Numbers are immutable
# ID of 5 and 6 remains same

my_list = [10]
print(f"my_list value: {my_list}, ID: {id(my_list)}")
my_list[0] = 20 # The content of the list is changed
print(f"my_list value: {my_list}, ID: {id(my_list)}") # ID remains same - Lists are mutable

