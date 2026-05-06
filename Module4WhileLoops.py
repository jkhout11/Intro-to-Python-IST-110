"""
File name: Module4WhileLoops.py
Short description: Practice using while loops to process numbers.
IST 140 Assignment: Module 4 Coding Practice
@author Jerry Khoutsavanh
@version 1.01
date of last revision: March 6, 2026
details of the revision: none
"""

# 1. Write a Python snippet to output the digits 0 - 9 to the command line.

print("Digits 0 through 9:")

num = 0

while num <= 9:
    print(num)
    num = num + 1


# 2. Prompt the user for a series of floating point numbers, followed by a -1 to quit.

print("\nEnter floating point numbers (-1 to quit)")

number = float(input("Enter a number: "))

minimum = number

while number != -1:

    if number < minimum:
        minimum = number

    number = float(input("Enter a number: "))

print("Minimum value:", minimum)


# 3. Prompt the user for a series of floating point numbers, followed by a -1 to quit.

print("\nEnter floating point numbers (-1 to quit)")

number = float(input("Enter a number: "))

minimum = number
maximum = number
total = 0
count = 0

while number != -1:

    if number < minimum:
        minimum = number

    if number > maximum:
        maximum = number

    total = total + number
    count = count + 1

    number = float(input("Enter a number: "))

average = total / count
range_value = maximum - minimum

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)
print("Range:", range_value)


"""
Output 1:
3
4
5
6


Output 2:
Enter floating point numbers (-1 to quit)
Enter a number: 5
Enter a number: 8
Enter a number: 2
Enter a number: -1
Minimum value: 2

Output 3:
Enter floating point numbers (-1 to quit)
Enter a number: 10
Enter a number: 4
Enter a number: 6
Enter a number: -1
Minimum: 4
Maximum: 10
Average: 6.666666666666667
Range: 6
"""