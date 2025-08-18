def safe_int_conversion(user_input):
    try:
        number = int(user_input)
    except ValueError:
        print(f"Error: '{user_input}' is not a valid number.")
    else:
        # This code runs ONLY if the try block above succeeds
        print(f"Success! Converted '{user_input}' to integer: {number}.")
        return number
    finally:
        print("Function finished.")

# Example 1: Successful conversion
safe_int_conversion("123")
# Output:
# Success! Converted '123' to integer: 123.
# Function finished.

# Example 2: Failed conversion
print("-" * 20)
safe_int_conversion("hello")
# Output:
# Error: 'hello' is not a valid number.
# Function finished.