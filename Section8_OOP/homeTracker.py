class SmartDevice():
    brand = "HomeTech"
    def __init__(self, device_name, power_status):
        self.brand = "CustomBrand"
        self.device_name = device_name
        self.power_status = power_status
    
    def get_status(self):
        if self.power_status == True:
            return f"{self.device_name} is ON - {self.brand}"
        else:
            return f"{self.device_name} is OFF - {self.brand}"