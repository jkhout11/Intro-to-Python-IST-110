"""
File name: SameSet.py
Short description: Write a function def sameSet(a, b) that checks whether two lists have the same elements in some
order, ignoring duplicates.
IST 140 Assignment: M06 - Coding Practice - Same Set
@author Jerry Khoutsavanh
@version 1.0 04/18/2025
date of last revision: 04/18/2025
details of the revision: none
"""

print("This program checks if two lists contain the same elements.")

# Check if a value is in a list
def contains(lst, value) :
    for item in lst :
        if item == value :
            return True
    return False

# Check if every item in list a is also in list b
def isSubset(a, b) :
    for item in a :
        if not contains(b, item) :
            return False
    return True

# Check if both lists have the same elements
def sameSet(a, b) :
    if isSubset(a, b) and isSubset(b, a) :
        return True
    else :
        return False

# Test lists
list1 = [1, 4, 9, 16, 9, 7, 4, 9, 11]
list2 = [11, 11, 7, 9, 16, 4, 1]

# Print results
print("List 1:", list1)
print("List 2:", list2)

if sameSet(list1, list2) :
    print("The two lists have the same elements.")
else :
    print("The two lists do not have the same elements.")

"""
Output 1:
This program checks if two lists contain the same elements.
List 1: [1, 4, 9, 16, 9, 7, 4, 9, 11]
List 2: [11, 11, 7, 9, 16, 4, 1]
The two lists have the same elements.

Output 2:
This program checks if two lists contain the same elements.
List 1: [1, 2, 3, 4, 5]
List 2: [5, 4, 3, 2, 1]
The two lists have the same elements.

Output 3:
This program checks if two lists contain the same elements.
List 1: [1, 2, 3]
List 2: [1, 2, 4]
The two lists do not have the same elements.
"""