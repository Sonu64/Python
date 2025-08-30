# The character '\r' (carriage return) moves the cursor to 
# the beginning of the current line without advancing to the next line. This allows 
# subsequent output to overwrite the text that was already on that line


# :02 -> This is a format specifier. The 0 means to pad the number with a leading zero if it is a single digit, 
# and the 2 specifies the total width of the field. 
# For example, if mins is 5, it will be formatted as 05. If it's 12, it will be 12


import time

while True:
    try:
        seconds = int(input("Enter the number of seconds: "))
        if (seconds < 0):
            print("Please enter a Positive number !")
            continue
    except ValueError as e:
        print("Please enter a number !")
        continue
    break



for remaining in range(seconds, 0, -1):
    mins = remaining // 60
    secs = remaining % 60
    timeFormat = f"{mins:02}:{secs:02}"
    print(f"Time Left: {timeFormat}",end="\r")
    time.sleep(1)

print("\nTime's Up !")