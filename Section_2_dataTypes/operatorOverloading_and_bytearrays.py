baseLiquid = ["water", "milk"]
extraFlavor = ["ginger"]
# Overloading + operator to work with Lists
fullMix = baseLiquid + extraFlavor
print(f"{fullMix}")


# Repetition
vegetables = ["ladyfinger"]
# The '*' operator repeats the list 5 times
repeated_list = vegetables * 5
print(repeated_list)  
# Output: ['ladyfinger', 'ladyfinger', 'ladyfinger', 'ladyfinger', 'ladyfinger']


# Create a bytearray from a string, encoded in 'utf-8'
data = bytearray("hello", 'utf-8')
print(data) # Output: bytearray(b'hello')

# You can change a byte in-place
# 72 is the ASCII value for 'H'
data[0] = 72
print(data) # Output: bytearray(b'Hello')

# You can also add more bytes to it
data.append(32)  # 32 is the ASCII value for a space
data.append(97)  # 97 is the ASCII value for 'a'
print(data) # Output: bytearray(b'Hello a')

# You can convert it back to a string
print(data.decode('utf-8')) # Output: Hello a
