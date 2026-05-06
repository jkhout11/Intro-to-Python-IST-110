#This is the program for recommending what golf club to use on the course depending on your skill level

def recommend_club(distance, skill):
    if skill == "above average":
        if distance >= 220:
            club = "Driver"
        elif distance >= 190:
            club = "3 Wood"
        elif distance >= 170:
            club = "3 Hybrid"
        elif distance >= 150:
            club = "6 Iron"
        elif distance >= 130:
            club = "7 Iron"
        elif distance >= 110:
            club = "8 Iron"
        elif distance >= 90:
            club = "9 Iron"
        elif distance >= 70:
            club = "Pitching Wedge"
        elif distance >= 40:
            club = "Sand Wedge"
        else:
            club = "Putter"

    elif skill == "average":
        if distance >= 200:
            club = "Driver"
        elif distance >= 170:
            club = "3 Wood"
        elif distance >= 150:
            club = "3 Hybrid"
        elif distance >= 130:
            club = "6 Iron"
        elif distance >= 110:
            club = "7 Iron"
        elif distance >= 90:
            club = "8 Iron"
        elif distance >= 70:
            club = "9 Iron"
        elif distance >= 50:
            club = "Pitching Wedge"
        elif distance >= 30:
            club = "Sand Wedge"
        else:
            club = "Putter"

    elif skill == "below average":
        if distance >= 180:
            club = "Driver"
        elif distance >= 160:
            club = "3 Wood"
        elif distance >= 140:
            club = "3 Hybrid"
        elif distance >= 120:
            club = "6 Iron"
        elif distance >= 100:
            club = "7 Iron"
        elif distance >= 80:
            club = "8 Iron"
        elif distance >= 60:
            club = "9 Iron"
        elif distance >= 40:
            club = "Pitching Wedge"
        elif distance >= 20:
            club = "Sand Wedge"
        else:
            club = "Putter"
    else:
        return "Invalid skill level entered. Please enter above average, average, or below average."

    return club

print("Welcome to the Golf Club Recommender!")
print("This program will help you choose the right club for your shot.")
print()

distance = int(input("Enter your distance to the hole in yards: "))
skill = input("Enter your skill level (above average, average, or below average): ").lower()

print()
recommendation = recommend_club(distance, skill)

print(f"Recommended club: {recommendation}")
print("Good luck with your shot!")

# Sample Output 1

# Welcome to the Golf Club Recommender!
# This program will help you choose the right club for your shot.
#
# Enter your distance to the hole in yards: 225
# Enter your skill level (above average, average, or below average): above average
#
# Recommended club: Driver
# Good luck with your shot!

# Sample Output 2

# Welcome to the Golf Club Recommender!
# This program will help you choose the right club for your shot.
#
# Enter your distance to the hole in yards: 115
# Enter your skill level (above average, average, or below average): average
#
# Recommended club: 7 Iron
# Good luck with your shot!

# Sample Output 3

# Welcome to the Golf Club Recommender!
# This program will help you choose the right club for your shot.
#
# Enter your distance to the hole in yards: 95
# Enter your skill level (above average, average, or below average): below average
#
# Recommended club: 7 Iron
# Good luck with your shot!