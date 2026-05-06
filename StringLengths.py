"""
StringLength
This program asks the user for a phrase and then prints the
length of that phrase (spaces count as characters).
"""

# ask user for a phrase
phrase = input("Please enter a phrase: ")

# get length of phrase
length = len(phrase)

# output result using formatting
print("Your phrase has a length of %d characters." % length)

"""
Sample 1
Please enter a phrase: Bad Bunny Forever
Your phrase has a length of 17 characters.


Process finished with exit code 0

Sample 2
Please enter a phrase: WE ARE PENN STATE
Your phrase has a length of 17 characters.

Process finished with exit code 0
"""