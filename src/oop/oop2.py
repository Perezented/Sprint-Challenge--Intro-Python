#
# object is constructed.

class GroundVehicle():
# Also change it so the num_wheels defaults to 4 if not specified when the
    def __init__(self, num_wheels = 4):
        self.num_wheels = num_wheels

# To the GroundVehicle class, add method drive() that returns "vroooom".
    # adding a method called drive to return the phrase 'vroooom'
    def drive(self):
        return "vroooom"


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"


# making another Motorcycle class that starts with 2 wheels instead of 4
# GroundVehicle is the parent class

# MOTORCYCLE
class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels = 2):
        super().__init__(num_wheels)
    # add a drive method for it with a different text noise
    def drive(self):
        return "BRAAAP!!"


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

for i in vehicles:
    i.drive()
    # print(i.drive())