"""
FuelCalculation
The program asks for gallons in the tank, mpg, and gas price.
Then it calculates how far the car can go and the cost to travel 50 miles.
"""

# get inputs from user
gallons = float(input("Enter number of gallons of gas in the tank: "))
mpg = float(input("Enter the fuel efficiency (miles per gallon): "))
price = float(input("Enter the price of gas per gallon: "))

# calculations
miles_possible = gallons * mpg
travel_cost = (50 / mpg) * price

# outputs with 2 decimals
print("You are able to travel %.2f miles on remaining fuel." % miles_possible)
print("It will cost $%.2f to travel 50 miles in the vehicle." % travel_cost)

""" 
Sample 1
Enter number of gallons of gas in the tank: 18
Enter the fuel efficiency (miles per gallon): 27
Enter the price of gas per gallon: 2.67
You are able to travel 486.00 miles on remaining fuel.
It will cost $4.94 to travel 50 miles in the vehicle.

Process finished with exit code 0

Sample 2
Enter number of gallons of gas in the tank: 32
Enter the fuel efficiency (miles per gallon): 18
Enter the price of gas per gallon: 2.67
You are able to travel 576.00 miles on remaining fuel.
It will cost $7.42 to travel 50 miles in the vehicle.

Process finished with exit code 0

Sample 3
Enter number of gallons of gas in the tank: 24
Enter the fuel efficiency (miles per gallon): 32
Enter the price of gas per gallon: 2.8
You are able to travel 768.00 miles on remaining fuel.
It will cost $4.38 to travel 50 miles in the vehicle.

Process finished with exit code 0

"""