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

