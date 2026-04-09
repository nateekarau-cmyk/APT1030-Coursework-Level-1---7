distance = float(input("Enter distance (km): "))

calculateFare = lambda d: 200 + (d * 50)

print("Total Fare:", calculateFare(distance))

""" This version uses a lambda function to calculate the fare. 
Functional programming focuses on using functions 
and expressions rather than classes or procedures. """