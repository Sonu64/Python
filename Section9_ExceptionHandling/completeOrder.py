class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    try:
        menu = {"masala":15, "ginger":40}
        if flavor not in menu:
            raise InvalidChaiError("That Chai is not available !")
        if not isinstance(cups, int):
            raise TypeError("The number of cups must be an integer !")
        
        total = menu[flavor] * cups

        print(f"Your Bill for {flavor} Chai is Rs.{total}.")
    except Exception as e:
        # For any runtime error
        print(f"ERROR !! {e}")
    finally:
        # Always runs
        print("Thank you ! Please come again !")

bill("ginger", 3)
bill("elaichi", 2)
