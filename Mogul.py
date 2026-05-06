"""
Mogul
This program asks for the cost of a property, the inflation rate,
and the appreciation rate, and then calculates the net profit after
one year. Sample runs are at the bottom.
"""

# get user inputs
userInput = input("Enter the cost of the property: ")
cost = float(userInput)

userInput = input("Enter the inflation rate: ")
inflation = float(userInput)

userInput = input("Enter the appreciation rate: ")
appreciation = float(userInput)

# calculate net profit
netProfit = (cost * appreciation) - (cost * inflation)

# print the result with 4 decimal places
print("Your investment's net profit is $%.2f." % netProfit)

"""
Sample 1
Enter the cost of the property: 420520
Enter the inflation rate: 0.05
Enter the appreciation rate: 0.10
Your investment's net profit is $21026.00.

Process finished with exit code 0

Sample 2
Enter the cost of the property: 520000
Enter the inflation rate: 0.08
Enter the appreciation rate: 0.10
Your investment's net profit is $10400.00.

Process finished with exit code 0

"""