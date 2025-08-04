beverage = "Hot Chocolate"
customerName = "Sonu"
print(f"Order for {customerName}: {beverage}")

# Indexing and Slicing Strings
description = "Hot and Chocolaty"
print(f"1st word: {description[:4]}")
print(f"Last word: {description[8:]}")
print(f"Reversed String: {description[::-1]}")
print(f"Skipping one letter (step of 2): {description[0:17:2]}")

# Encoding strings
myName = "সৌরকান্তি"
enCodedName = myName.encode("utf-8")
decodedName = enCodedName.decode("utf-8")
print(f"Normally printing: {myName}")
print(f"Encoded Version: {enCodedName}")
print(f"Decoded Name: {decodedName}")