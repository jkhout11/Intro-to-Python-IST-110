"""
File name: M05CodingPracticeMathFunctions.py
Short description: Code to find the smallest of 3 numbers and calculate their average.
IST 140 Assignment: M05 Coding Practice - Math Functions
@author Jerry Khoutsavanh
@version 1.01 03/21/2025
date of last revision: 03/22/2025
"""

def smallest(x, y, z) :
    if x <= y and x <= z :
        return x
    elif y <= x and y <= z :
        return y
    else :
        return z

def average(x, y, z) :
    return (x + y + z) / 3.0

def main() :
    print("Enter three numbers...")
    x = float(input("First number: "))
    y = float(input("Second number: "))
    z = float(input("Third number: "))

    print("Smallest:", smallest(x, y, z))
    print("Average: %.3f" % average(x, y, z))

main()

"""
Output 1:
Enter three numbers...
First number: 5
Second number: 10
Third number: 3
Smallest: 3.0
Average: 6.000

Output 2:
Enter three numbers...
First number: 7
Second number: 2
Third number: 9
Smallest: 2.0
Average: 6.000

Output 3:
Enter three numbers...
First number: 1
Second number: 1
Third number: 1
Smallest: 1.0
Average: 1.000
"""