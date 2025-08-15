class Chai:
    def __init__(self, chaiType, strength):
        self.type = chaiType
        self.strength = strength

class GingerChai(Chai):
    # Couple of code duplication is needed
    def __init__(self, chaiType, strength, spiceLevel):
        self.type = chaiType
        self.strength = strength
        self.spiceLevel = spiceLevel

# Method 1 to access Base Class, - EXPLICIT CALL to the class constructor
class KesarChai(Chai):
    def __init__(self, chaiType, strength, spiceLevel):
        Chai.__init__(self, chaiType, strength)
        self.spiceLevel = spiceLevel

# Method 2 to access Base Class, - Using super()
class MalaiChai(Chai):
    def __init__(self, chaiType, strength, spiceLevel):
        super().__init__(self, chaiType, strength)
        self.spiceLevel = spiceLevel