"""
File name: List_Calculations.py
Short description: Program that gets 6 student scores and calculates the average using functions.
IST 140 Assignment: M06 - PA - ListCalculations
@author Jerry Khoutsavanh
@version 1.0 04/18/2025
date of last revision: 04/18/2025
details of the revision: none
"""

print("This program will get 6 student scores and calculate the average.")

# Function to get 6 scores from the user and return them as a list
def getScores() :
    scores = []
    for i in range(6) :
        score = float(input("Enter score " + str(i + 1) + ": "))
        scores.append(score)
    return scores

# Function to calc the average of the scores
def calcAverage(scores) :
    total = 0
    for score in scores :
        total = total + score
    return total / len(scores)

# Function to print the average
def printAverage(average) :
    print("The average score is %.2f" % average)

scores = getScores()
average = calcAverage(scores)
printAverage(average)

"""
Output 1:
This program will get 6 student scores and calculate the average.
Enter score 1: 85
Enter score 2: 90
Enter score 3: 78
Enter score 4: 92
Enter score 5: 88
Enter score 6: 76
The average score is 84.83

Output 2:
This program will get 6 student scores and calculate the average.
Enter score 1: 70
Enter score 2: 65
Enter score 3: 80
Enter score 4: 75
Enter score 5: 90
Enter score 6: 85
The average score is 77.50

Output 3:
This program will get 6 student scores and calculate the average.
Enter score 1: 100
Enter score 2: 95
Enter score 3: 88
Enter score 4: 92
Enter score 5: 97
Enter score 6: 91
The average score is 93.83
"""