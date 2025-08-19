class OutOfIngredientsError(Exception):
    print(f"You have run out of ingredients !")

def makeChai(milk, sugar):
    def __init__(self):
        if milk == 0 or sugar == 0:
            raise OutOfIngredientsError("Out of Ingredients :( ")
        else:
            self.milk = milk
            self.sugar = sugar

tea1 = makeChai(2, 3)
tea2 = makeChai(1, 0)