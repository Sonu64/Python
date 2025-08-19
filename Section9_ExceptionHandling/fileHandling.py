# Older way of handling files in Python
try:
    data = open("data.txt", "w")
    print("File Opened, writing to file...")
    data.write("File Loaded to Memory, Written, then Unloaded back !")
except Exception as e:
    print(e)
finally:
    data.close()
    print("File Closed")
# Newer way using with keyword. Handles opening and closing on its own
with open("data.txt", "a+") as file:
    print("\nOpening File again for Appending...")
    file.write("Hello, world !")
    print("File Closed")