"""
File name: Is_List_Sorted.py
Short description: Function to check if a list of integers is sorted in descending order.
IST 140 Assignment: M06 - PA - isListSorted
@author Jerry Khoutsavanh
@version 1.0 04/18/2025
date of last revision: 04/18/2025
details of the revision: none
"""

print("This program checks if a list is sorted in descending order.")

def in_order(nums) :
    for i in range(len(nums) - 1) :
        if nums[i] < nums[i + 1] :
            return False
    return True

if __name__ == '__main__' :
    # Test out of order example
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1) :
        print('In descending order')
    else :
        print('Not in order')

    # Test in order example
    nums2 = [10, 8, 7, 6, 5]
    if in_order(nums2) :
        print('In descending order')
    else :
        print('Not in order')

"""
Output 1:
This program checks if a list is sorted in descending order.
Not in order
In descending order

Output 2:
This program checks if a list is sorted in descending order.
Not in order
In descending order

Output 3:
This program checks if a list is sorted in descending order.
Not in order
In descending order
"""