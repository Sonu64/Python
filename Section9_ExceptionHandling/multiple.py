def processOrder(item, quantity):
    menu = {"masala":20, "kesar":30, "ginger":30}
    try:
        price = menu[item]
        cost = int(price) * int(quantity)
        return price
    except KeyError:
        return f"Sorry, {item} is not in our Menu"
    except ValueError:
        return f"{quantity} is not a valid quantity, it must be a number"

print(processOrder("malai", 3)) # KeyError
print(processOrder("ginger", "two")) # ValueError