availableSizes = ["small", "medium", "large"]

if (askedSize := input("Enter Cup size: ").lower()) in availableSizes:
    print(f"User wants {askedSize}.")
else: 
    print(f"User wants some unknown size")


flavors = ["Vanilla", "Chocolate", "Mango"]
while (flavor := input("Choose a flavor: ")) not in flavors:
    print("Sorry, Flavor not available !")
print(f"You chose {flavor} flavor")