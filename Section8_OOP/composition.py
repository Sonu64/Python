class Engine:
    def start(self):
        print("Engine started!")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car has an Engine (composition)

    def start(self):
        print("Car starting")
        self.engine.start()  # Delegate starting responsibility to the engine

# Usage
my_car = Car()
my_car.start()
