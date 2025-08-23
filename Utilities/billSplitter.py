numOfPeople = int(input("Enter number of people: "))
names = []

def getFloat(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError as e:
            print("Valueerror")
            print(e)
        except TypeError as t:
            print("Typeerror")
            print(t)
        finally:
            print("Thank you !")

for i in range(numOfPeople):
    name = input(f"Enter Person {i+1} Name: ")
    names.append(name)

totalBill = getFloat("Enter total Bill amount in number: ");
split = totalBill / numOfPeople
split = round(split, 2)

print("\n", "*"*60, "\n")
for name in names:
    print(f"{name} owes: Rs. {split}")
print("\n", "*"*60);