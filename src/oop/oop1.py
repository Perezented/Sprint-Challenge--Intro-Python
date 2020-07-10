# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


# looks like a VEHICLE is the main parent class for all of the following classes
class Vehicle:
    def __init__(self, name, vehicleType):
        self.name = name
        self.vehicleType = vehicleType
# FLIGHTVEHICLE fom the main class, Vehicle
class FlightVehicle(Vehicle):
    def __init__(self, name, vehicleType):
        super().__init__(name, vehicleType)


# which in turn has two subclasses below that
# STARSHIP branched off of FlightVehicle
class Starship(FlightVehicle):
    def __init__(self, name, vehicleType, spaceshipType):
        super().__init__(name, vehicleType)
        self.spaceshipType = spaceshipType
# AIRPLANE branched off of FlightVehicle
class Airplane(FlightVehicle):
    def __init__(self, name, vehicleType,  airplaneType):
        super().__init__(name, vehicleType)
        self.airplaneType = airplaneType

# GROUNDVEHICLE branches off of the main branched
class GroundVehicle(Vehicle):
    def __init__(self, name, vehicleType):
        super().__init__(name, vehicleType)
# Car and Motorcycle branch off of a GroundVehicle
# CAR
class Car(GroundVehicle):
    def __init__(self, name, vehicleType, carType):
        super().__init__(name, vehicleType)
        self.carType = carType

# MOTORCYCLE
class Car(GroundVehicle):
    def __init__(self, name, vehicleType, motorcycleType):
        super().__init__(name, vehicleType)
        self.motorcycleType = motorcycleType
