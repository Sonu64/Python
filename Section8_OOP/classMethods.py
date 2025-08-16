class ChaiOrder:
    def __init__(self, teaType, sweetness, size):
        self.teaType = teaType
        self.sweetness = sweetness
        self.size = size

    # One main use-case of class methods is to create alternative constructors
    # which under-the-hood calls the original constructor
    @classmethod
    def fromDict(cls, orderData):
        orderDict = {
            "teaType":orderData['teaType'],
            "sweetness":orderData['sweetness'],
            "size":orderData['size']
        }
        return cls(
            orderDict['teaType'],
            orderDict['sweetness'],
            orderDict['size']
        )
    
    @classmethod
    def fromString(cls, orderString):
        teaType, sweetness, size = orderString.split(",")
        return cls(teaType, sweetness, size)