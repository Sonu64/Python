# This function will be tested by the evaluation system. Do not modify the function name or parameters.
def check_loan_eligibility(age: int, income: float) -> str:
    # Write your code below this line
    if age >= 21:
        if income >= 25000:
            return "Eligible for loan"
        else:
            return "Not eligible: Income too low"
    else:
        return "Not eligible: Age must be 21 or above"
    pass