#OOP Implementation of a Ride-Hailing Pricing Engine
class Ride:

    def __init__(self, distance):
        self.distance = distance

    def calculateFare(self):
        return 200 + (self.distance * 50)


distance = float(input("Enter distance (km): "))

ride1 = Ride(distance)

print("Total Fare:", ride1.calculateFare())