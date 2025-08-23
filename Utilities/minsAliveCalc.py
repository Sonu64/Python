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
        except TypeError as e:
            print("Error !")
            print(e)
        except ValueError as e:
            print("ValueError")
            print(e)

choice = "y"
while choice == "y":
    age = getFloat("\nEnter your age: ")
    days, hours, mins = calculateMins(age)
    print("*"*40)
    print("You are - ")
    print(f"{days} Days, {hours} Hours and {mins} Minutes Old")

    choice = input("\nDo you want to calculate again ? (y/n): ").strip().lower()
    while choice != "y" and choice != "n":
        choice = input("\nPlease enter Valid choice ? (y/n): ").strip().lower()

print("*"*40)