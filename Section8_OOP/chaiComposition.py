# Base class BaseChai
class BaseChai:
    def __init__(self, type_):
        self.type = type_
    def prepare(self):
        print(f"Preparing {self.type} chai....")

# Inheriting from BaseChai, It "is-a" BaseChai
class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, cloves.")

# Uses instance of BaseChai inside it, It "has-a" BaseChai component
class ChaiShop:
    # Not yet creating object like BaseChai("Regular"), just keeping an instance
    chai_cls = BaseChai

    # self.chai is becoming an object of BaseChai
    def __init__(self):
        self.chai = self.chai_cls("Regular")

    # As self.chai is object of BaseChai, it will have the property of 'type'
    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()



# Combining Inheritance and Composition - FancyChaiShop "is-a" ChaiShop and "has-a" MasalaChai
class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai

# Creating objects of classes
shop = ChaiShop()
fancy = FancyChaiShop()

shop.serve() # OUTPUT: Serving Regular Chai in the shop, Preparing Regular Chai....
fancy.serve() # OUTPUT: Serving Regular Chai in the shop, Preparing Regular Chai....
fancy.chai.add_spices()