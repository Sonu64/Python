# This function will be tested automatically. 
# Do not change the function name or parameters.
def simulate_atm_withdrawals(balance: int, withdrawals: list[int]) -> list[str]:
    # Write your code below this line
    result = []
    i = 0
    while i in range(len(withdrawals)):
        if (balance >= withdrawals[i]):
            balance -= withdrawals[i]
            result.append(f"Withdrawn: {withdrawals[i]}")
        else:
            result.append(f"Insufficient funds for requested amount: {withdrawals[i]}")
        i += 1
    result.append(f"Remaining Balance: {balance}")
    return result
    pass

print(simulate_atm_withdrawals(100, [10, 80, 200]))