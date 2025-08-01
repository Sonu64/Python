books = ("Feluda", "Byomkesh", "Kakababu")
(book1, book2, book3) = books
print(f"Books are {book1}, {book2}, {book3}")

# Behind the scenes python uses tuples to assign variables as followed
name, number = "Sonu", "70478XXXXX"
print(f"Details: {name}, Ph. no.: {number}")
# Swapping vars
name, number = number, name
print(f"Details: {name}, Ph. no.: {number}")

# Membership testing using 'in'
print(f"Is Kiriti in books ? {"Kiriti" in books}")
print(f"Is Byomkesh in books ? {"Byomkesh" in books}")