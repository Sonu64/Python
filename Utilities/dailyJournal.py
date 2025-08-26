import datetime

entry = input("What did you learn today: ")
rating = input("Rate your productivity today (Optional) (0-5): ")

now = datetime.datetime.now()
date_str = now.strftime("%Y-%m-%d - %I:%M %p")

output = "*" * 50 + "\n"
output = f"\nDate: {date_str}"
if rating: 
    output += f"\nProductivity rating: {rating}\n{entry}"
else:
    output += f"\n{entry}\n"

with open("journal.txt", "a", encoding="utf-8") as f:
    f.write(output)

print("Your Journal entry has been added to journal.txt !")