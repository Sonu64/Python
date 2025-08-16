class ChaiOrder:
    def __init__(self, teaType, sweetness, size):
        self.teaType = teaType
        self.sweetness = sweetness
        self.size = size

    # One main use-case of class methods is to create alternative constructors
    # which under-the-hood calls the original constructor
    @classmethod
    def fromDict(cls, orderData):
        return cls(
            orderData['teaType'],
            orderData['sweetness'],
            orderData['size']
        )
    
    @classmethod
    def fromString(cls, orderString):
        teaType, sweetness, size = orderString.split(",")
        return cls(teaType, sweetness, size)
    
    def describeOrder(self):
        return f"{self.teaType} Tea with {self.sweetness} sweetness and cup size is {self.size}."
    

order1 = ChaiOrder.fromDict({"teaType":"Masala","sweetness":"Medium", "size":"Large"})
order2 = ChaiOrder.fromString("Ginger, Low, Small")

print(order1.describeOrder())
print(order2.describeOrder())

# Using available dunders on the objects

#__dict__ to show the passed properties in dictionary format
print(f"Order 1 Properties: {order1.__dict__}")
print(f"Order 2 Properties: {order2.__dict__}")



