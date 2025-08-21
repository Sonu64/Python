from datetime import date
# Getting the information
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ").strip()
proffession = input("Enter your Proffession: ").strip()
hobby = input("Enter your hobby: ").strip()

output = f"""Hello, my name is {name}. I am {age} years old and live in {city}.
I work as a {proffession} and I absolutely enjoy {hobby} during my free time."""
loginInfo = f"Logged in On: {date.today()}"
border = "*" * 50
print(f"\n{border}\n{output}\n\n{loginInfo}\n{border}\n")