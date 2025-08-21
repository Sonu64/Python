from datetime import date
# Getting the information
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
proffession = input("Enter your Proffession: ")
hobby = input("Enter your hobby: ")

output = f"""Hello, my name is {name}. I am {age} years old and live in {city}.
I work as a {proffession} and I absolutely enjoy {hobby} during my free time."""

print(output)
print(f"Logged in On: {date.today()}")