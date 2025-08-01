fruits = ["mango", "banana"]
fruits.append("apple")
fruits.remove("banana")
print(f"{fruits}")
veggies = ["cauliflower", "onion"]

fruits.extend(veggies)
print(f"{fruits}")

fruits.insert(1, "ginger")
print(f"{fruits}")

lastAdded = fruits.pop()
print(f"{fruits}, {lastAdded}")

fruits.reverse()
print(f"{fruits}")

nums = [1, 2, 3, 4, 5]
print(f"Maximum:{max(nums)}, Minimum:{min(nums)}")