class ChaiOrder:
    # Constructor
    def __init__(self, masala, noOfCups):
        self.masala = masala
        self.noOfCups = noOfCups
    # Methods
    def describe(self):
        return f"{self.noOfCups} Cups of {self.masala} Tea."

gingerTea = ChaiOrder("Ginger", 5)
kesarTea = ChaiOrder("Kesar", 10)

print(gingerTea.describe())
print(kesarTea.describe())