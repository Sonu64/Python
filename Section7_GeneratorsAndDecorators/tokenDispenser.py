def token_dispenser(start: int = 1):
    """
    An infinite generator that dispenses incrementing tokens.
    It can be reset by sending a new value and handles graceful closure.
    """
    token = start
    print("Dispenser started...")
    
    try:
        while True:
            # Yield the current token and wait for a new value to be sent
            new_token = yield token
            
            # If a value was sent (i.e., not None), reset the token
            if new_token is not None:
                token = new_token
            else:
                # If no value was sent, increment the token as usual
                token += 1
                
    except GeneratorExit:
        # Handle the .close() method by printing a message
        print("Dispenser closed.")



# Create a dispenser instance
dispenser = token_dispenser(start=100)

# Use next() to get the first few tokens
# The first call to next() starts the generator
print(f"Token: {next(dispenser)}")  # Output: Token: 100
print(f"Token: {next(dispenser)}")  # Output: Token: 101

# Use send() to reset the token number
# The sent value (1) becomes the new token, and the generator yields it
print(f"Token: {dispenser.send(1)}") # Output: Token: 1

# Continue using next(), which now increments from the new value
print(f"Token: {next(dispenser)}")  # Output: Token: 2
print(f"Token: {next(dispenser)}")  # Output: Token: 3

# Close the generator to trigger the cleanup message
dispenser.close()
# Output: Dispenser closed.

# Attempting to use the dispenser after it's closed will raise a StopIteration error
try:
    next(dispenser)
except StopIteration:
    print("Generator is stopped.")
