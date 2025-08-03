# This function will be tested automatically. 
# Do not change the function name or parameter type.
def verify_age(age_str: str) -> str:
    # Write your code here
    age_str = int(age_str)
    return "Access Granted" if (age_str >= 18) else "Access Denied"
    pass