chaiMenu = {"masala":30, "ginger":30}

try:
    print(chaiMenu['kesar'])
except KeyError:
    print(f"Key does not exist !")

print("Program over")