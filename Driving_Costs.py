"""
File name: driving_costs.py
Short description: Program that calculates the cost to drive certain miles based on mpg and gas price.
IST 140 Assignment: driving_costs
@author Jerry Khoutsavanh
@version 1.0 03/28/2025
date of last revision: 03/28/2025
details of the revision: none
"""

def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven) :
    return (miles_driven / miles_per_gallon) * dollars_per_gallon

miles_per_gallon = float(input("Enter miles per gallon: "))
dollars_per_gallon = float(input("Enter dollars per gallon: "))

print(f'Cost for 10 miles: ${driving_cost(miles_per_gallon, dollars_per_gallon, 10.0):.2f}')
print(f'Cost for 50 miles: ${driving_cost(miles_per_gallon, dollars_per_gallon, 50.0):.2f}')
print(f'Cost for 400 miles: ${driving_cost(miles_per_gallon, dollars_per_gallon, 400.0):.2f}')

"""
Output 1:
Enter miles per gallon: 20.0
Enter dollars per gallon: 3.1599
Cost for 10 miles: $1.58
Cost for 50 miles: $7.90
Cost for 400 miles: $63.20

Output 2:
Enter miles per gallon: 25.0
Enter dollars per gallon: 3.50
Cost for 10 miles: $1.40
Cost for 50 miles: $7.00
Cost for 400 miles: $56.00

Output 3:
Enter miles per gallon: 30.0
Enter dollars per gallon: 4.00
Cost for 10 miles: $1.33
Cost for 50 miles: $6.67
Cost for 400 miles: $53.33
"""