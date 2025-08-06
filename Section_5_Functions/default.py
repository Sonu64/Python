def chaiOrder(order = None):
    if order == None:
        order = []
        print(f"No order placed !")
    else:
        print(f"Order is {order}")

chaiOrder()
chaiOrder(["Ginger tea", "Masala Chai", "Kesar chai", "Black tea"])