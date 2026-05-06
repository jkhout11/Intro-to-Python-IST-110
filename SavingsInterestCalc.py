"""
Savings and Interest Calc
This program asks for the principal, interest rate, and years.
Then it computes simple interest using S = p * (1 + r * t).
"""
# read principal as string then convert
userInput = input("Please enter the amount you are saving: ")
p = float(userInput)

# read interest rate
userInput = input("Please enter the yearly interest rate: ")
r = float(userInput)

# read years
userInput = input("Please enter the number of years you are saving: ")
t = float(userInput)

# compute simple interest
S = p * (1 + r * t)

# convert rate to percent
ratePercent = r * 100

# formatted output using percentage operator
print("The current yearly interest rate is %.2f%%. At the end of year %d, you will receive $%.2f if you deposit $%.2f right now."
      % (ratePercent, t, S, p))

"""
Sample Run 1 
Please enter the amount you are saving: 2000
Please enter the yearly interest rate: 1.2
Please enter the number of years you are saving: 30
The current yearly interest rate is 120.00%. At the end of year 30, you will receive $74000.00 if you deposit $2000.00 right now.

Process finished with exit code 0

Sample Run 2
Please enter the amount you are saving: 100000
Please enter the yearly interest rate: 1.1
Please enter the number of years you are saving: 3
The current yearly interest rate is 110.00%. At the end of year 3, you will receive $430000.00 if you deposit $100000.00 right now.

Process finished with exit code 0
"""