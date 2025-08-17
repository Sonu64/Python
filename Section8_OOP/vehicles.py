class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def get_engine_info(self):
        return f"{self.horsepower} HP Engine"

class Vehicle:
    total_vehicles = 0
    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.engine = Engine(150)
        self._rental_price = 0
        Vehicle.total_vehicles += 1
    
    def get_details(self):
        return f"{self.brand}, {self.model}, {self.engine.get_engine_info()}"
        
    @staticmethod
    def get_vehicle_type():
        return "Generic Vehicle"
    
    @classmethod
    def get_total_vehicles(cls):
        return cls.total_vehicles
    
    @property
    def rental_price(self):
        return self._rental_price
    
    @rental_price.setter
    def rental_price(self, rp):
        if rp > 0:
            self._rental_price = rp
    
class Car(Vehicle):
    def __init__(self, brand, model, engine, seats):
        super().__init__(brand, model, engine)
        self.seats = seats
    def get_details(self):
        return f"{super().get_details()} - Seats: {self.seats}"