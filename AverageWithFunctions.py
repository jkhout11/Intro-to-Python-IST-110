"""
File name: AverageWithFunctions.py
Short description: Program that gets 3 grades from the user and calculates the average using functions.
IST 140 Assignment: AverageWithFunctions
@author Jerry Khoutsavanh
@version 1.00 03/28/2025
date of last revision: 03/28/2025
details of the revision: none
"""

def printDescription() :
    print("This program will ask you for three grades and calculate their average.")

def getTotal() :
    grade1 = float(input("Enter the first grade: "))
    grade2 = float(input("Enter the second grade: "))
    grade3 = float(input("Enter the third grade: "))
    total = grade1 + grade2 + grade3
    return total

def calcAverage(total) :
    return total / 3.0

def printResults(total, average) :
    print("The total of your grades is %.2f" % total)
    print("Your average grade is %.2f" % average)

printDescription()
total = getTotal()
average = calcAverage(total)
printResults(total, average)

"""
Output 1:
This program will ask you for three grades and calculate their average.
Enter the first grade: 85
Enter the second grade: 90
Enter the third grade: 78
The total of your grades is 253.00
Your average grade is 84.33

Output 2:
This program will ask you for three grades and calculate their average.
Enter the first grade: 72
Enter the second grade: 68
Enter the third grade: 91
The total of your grades is 231.00
Your average grade is 77.00

Output 3:
This program will ask you for three grades and calculate their average.
Enter the first grade: 95
Enter the second grade: 88
Enter the third grade: 76
The total of your grades is 259.00
Your average grade is 86.33
"""