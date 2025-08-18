def brewChai(item):
    menu = ["masala", "kesar", "ginger"]
    if item not in menu:
        raise ValueError("Error ! Chai not in Menu") 
        # maybe RuntimeError if we don't know the error type
    print(f"Brewing {item} Chai...")

brewChai("elaichi")   # Error
    