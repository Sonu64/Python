import string
import getpass
import random

specialChars = ["`", "!", "~", "@", "#", "$", "%", "^", "*", "&"] # string.punctuation

def checkPasswordStrength(password):
    
    issues = []

    # Checking Length
    if len(password) < 8:
        issues.append("Password too Short ! (Minimum 8 characters)")
    
    # Checking lowercase uppercase
    oneLower = False
    oneUpper = False
    for c in password:
        if c.islower():
            oneLower = True;
            break;
    for c in password:
        if c.isupper():
            oneUpper = True;
            break;
    if not oneLower:
        issues.append("- Missing a Lowercase Letter")
    if not oneUpper:
        issues.append("- Missing an Uppercase Letter")


    # Checking for digits
    containsDigit = False
    for c in password:
        if c.isdigit():
            containsDigit = True
    if not containsDigit:
        issues.append("- Missing a Digit")



    # Checking special characters
    containsSpecialChar = False
    for c in password:
        if c in specialChars:
            containsSpecialChar = True
            break
    if not containsSpecialChar:
        issues.append("- Missing Special Character")

    return issues

def suggestStrongPassword(length = 12):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits
    password = ""
    for i in range(length):
        chosenChar = chars[random.randint(0, len(chars))] # or use random.choice(chars)
        password += chosenChar
    return password

def manageApp():
    while True:
        print("\n------ Password Strength Checker and Suggestion Tool ------")
        print("1. Check Password Strength")
        print("2. Suggest Strong Password")
        print("3. Exit App")
        choice = int(input("Choose an Option [1-3]: "))
        match choice:
            case 1:
                pwd = getpass.getpass("\nEnter Password: ")
                issues = checkPasswordStrength(pwd)
                if issues:
                    print("Umm...Issues in your password are..")
                    for issue in issues:
                        print(issue)
                    print("You can use a password like " + suggestStrongPassword())
                else:
                    print("No issues found ! Your Password Looks Strong enough !")
            case 2:
                length = int(input("Enter your preferred password length: "))
                suggestedPwd = suggestStrongPassword(length)
                print("You can use something like " + suggestedPwd)
            case 3:
                print("Exiting App...")
                break;
            case _:
                print("Invalid choice !")

manageApp()
