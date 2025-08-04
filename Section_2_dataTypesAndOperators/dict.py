# Create a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Access a value using its key
print(person["name"])  # Output: Alice

# Add a new key-value pair
person["email"] = "alice@example.com"
print(person) # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'email': 'alice@example.com'}

# Modify an existing value
person["age"] = 31
print(person["age"]) # Output: 31

# Print all keys
print(person.keys())  # Output: dict_keys(['name', 'age', 'city', 'email'])
# Print all items
print(person.values()) # Output: dict_values(['Alice', 31, 'New York', 'alice@example.com'])

# Key 'country' does not exist, Safely retrieving via get()
country = person.get("country", "404 not found")
print(country) # Output: Unknown

# Popping any item
removed_age = person.pop("age")
print(removed_age) # Output: 31
print(person)      # Output: {'name': 'Alice', 'city': 'New York', 'email': 'alice@example.com'}

# Deleting
my_dict = {'name': 'Bob', 'age': 25, 'city': 'London'}
print(my_dict) # Output: {'name': 'Bob', 'age': 25, 'city': 'London'}
del my_dict['age']
print(my_dict) # Output: {'name': 'Bob', 'city': 'London'}

#Popping last item
my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
# Remove and retrieve the last item
last_item = my_dict.popitem()
print(f"Removed item: {last_item}")
print(f"Updated dictionary: {my_dict}")