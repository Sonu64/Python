class Chaicup:
    size = 150 #ml

    def describe(self):
        return f"A {self.size}ml chai cup"
    

cup = Chaicup()
# When calling via objects, parameter self automatically set to that object's reference
print(cup.describe())
# When calling directly via class, an object needs to be passed as parameter as SELF 
print(Chaicup.describe(cup))

cup_two = Chaicup()
cup_two.size = 100
print(Chaicup.describe(cup_two))