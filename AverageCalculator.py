"""This is the Average Calculator:
that prompts the user with four separate prompts for four numbers using float values,
computes the average of those 4 floats using a float for the average, and then prints out explanatory text,
the four numbers, and their average, printed with 2 decimal places"""

#Numbers gotten from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))

#Find Average
avg = (num1 + num2 + num3 + num4) / 4

#Show results w/ 2 decimal places
print(f"The average of the numbers {num1:.2f}, {num2:.2f}, {num3:.2f}, and {num4:.2f} is {avg:.2f}.")

""" Enter first number: 34.6
Enter second number: 45.7
Enter third number: 36.8
Enter fourth number: 64.2
The average of the numbers 34.60, 45.70, 36.80, and 64.20 is 45.33.

Process finished with exit code 0
"""
""" Enter first number: 32.5
Enter second number: 44.6
Enter third number: 54.3
Enter fourth number: 56.8
The average of the numbers 32.50, 44.60, 54.30, and 56.80 is 47.05.

Process finished with exit code 0 """

""" Enter first number: 78.7
Enter second number: 82.4
Enter third number: 88.3
Enter fourth number: 85.6
The average of the numbers 78.70, 82.40, 88.30, and 85.60 is 83.75.

Process finished with exit code 0
"""