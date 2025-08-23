def calculateMins(age):
    DAYS_IN_AN_YEAR = 365.25
    HOURS_IN_A_DAY = 24.0
    MINUTES_IN_AN_HOUR = 60

    days = age * DAYS_IN_AN_YEAR
    hours = days * HOURS_IN_A_DAY
    mins = hours * MINUTES_IN_AN_HOUR

    return round(days), round(hours), round(mins)


def getFloat(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError as e:
            print(e)
            return

choice = "y"
while choice == "y":
    age = getFloat("Enter your age: ")
    days, hours, mins = calculateMins(age)
    print("\n","*"*40)
    print("You are - ")
    print(f"{days} Days, {hours} Hours and {mins} Minutes Old")

    choice = input("\nDo you want to calculate again ? (y/n): ").strip().lower()
    while choice != "y" and choice != "n":
        choice = input("\nPlease enter Valid choice ? (y/n): ").strip().lower()

print("\n","*"*40)