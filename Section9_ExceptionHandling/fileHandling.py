# Older way of handling files in Python
try:
    data = open("datas.txt", "w")
    data.write("File Loaded to Memory, Written, then Unloaded back !")
except Exception as e:
    print(e)
finally:
    data.close()

