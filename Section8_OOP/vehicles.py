class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def get_engine_info():
        return f"{self.horsepower} HP Engine"

class Vehicle:
    total_vehicles = 0
    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.engine = Engine(150)
        total_vehicles += 1
    
    def get_details(self):
        return [self.brand, self.model, self.get_engine_info()]
        
    @staticmethod
    def get_vehicle_type():
        return "Generic Vehicle"
    
    @classmethod
    def get_total_vehicles(cls):
        return cls.total_vehicles
    
    
    