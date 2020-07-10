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
    def __init__(self, name, vType):
        self.name = name
        self.vType = vType
# FLIGHTVEHICLE fom the main class, Vehicle


# which in turn has two subclasses below that
# STARSHIP branched off of FlightVehicle

# AIRPLANE branched off of FlightVehicle


# GROUNDVEHICLE branches off of the main branched

# Car and Motorcycle branch off of a GroundVehicle
# CAR

# MOTORCYCLE