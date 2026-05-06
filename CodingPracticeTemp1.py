"""
File name: CodingPracticeTemp1.py
Short description: Determines whether water is solid, liquid, or gas based on temperature.
IST 140 Assignment: M03 - Coding Practice - Temperature Part 1
@author Jerry Khoutsavanh
@version 1.01 02/25/2026
date of last revision: none
details of the revision: none
"""

# Program description
print("This program determines whether water is solid, liquid, or gas at a given temperature.")

# Input
temp = float(input("Enter temperature: "))
scale = input("Enter C for Celsius or F for Fahrenheit: ")

# Determine state using Celsius rules
if scale.upper() == "C":
    if temp > 100:
        state = "gas"
    elif temp > 0:
        state = "liquid"
    else:
        state = "solid"

# Determine state using Fahrenheit rules
elif scale.upper() == "F":
    if temp > 212:
        state = "gas"
    elif temp > 32:
        state = "liquid"
    else:
        state = "solid"

    # Also convert Fahrenheit to Celsius
    celsius = (temp - 32) * 5/9
    print("Converted to Celsius: %.2f C" % celsius)

else:
    state = "invalid scale"

# Output result
print("Water is", state, "at this temperature.")

"""
Output 1:
Enter temperature: 90
Enter C for Celsius or F for Fahrenheit: F
Converted to Celsius: 32.22 C
Water is liquid at this temperature.

Output 2:
Enter temperature: 20
Enter C for Celsius or F for Fahrenheit: F
Converted to Celsius: -6.67 C
Water is solid at this temperature.

Output 3:
Enter temperature: 230
Enter C for Celsius or F for Fahrenheit: F
Converted to Celsius: 110.00 C
Water is gas at this temperature.
"""