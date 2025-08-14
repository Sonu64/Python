# Parent Class
class BaseClass:
    def __init__(self, username):
        self.username = username
    def printDetails(self):
        return f"Username: {self.username}"
    
# Child Class, inheriting from parent class
class ChildClass(BaseClass):
    def addRoles(self):
        self.role = "Robotics Software Engineer"

sonu = ChildClass("Sonu")
print(sonu.printDetails())
sonu.addRoles()
print(sonu.role)
