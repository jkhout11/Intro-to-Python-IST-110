# 1. Write a Python code snippet that prints your name and your major.
# Each piece of information should be on a separate line.
print("Jerry Khoutsavanh")
print("Computer Science")
print()
# 2. A ferry has a maximum capacity of 200 tons. Assume there are 8 vehicles onboard, each weighing 20 tons.
# Write a Python snippet to calculate the remaining weight capacity of the ferry.
# Output should be in this format:
# "The ferry can still hold ___ tons."
max_cap = 200
vehicles_onboard = 8
vehicle_weight = 20
total_vehicle_weight = vehicles_onboard * vehicle_weight
remaining_weight_cap = max_cap - total_vehicle_weight
print("The ferry can still hold", remaining_weight_cap, "tons")
# 3. Write an email to an LA asking for help on an assignment.
# Include a salutation, three sentences in the body, and a polite closing.

# Example:
# Hi [LA's Name],
#
# I hope this email finds you well. I am having trouble understanding the concept of input statements in Python. Would you be able to meet after class to go over it with me?
#
# Thank you,
# [Your Name]
print()
la_name = "Bob"
sender_name = "Jerry"
print("Hi", la_name, ",")
print()

print("I need help with the assignment. Can you meet with me after class? Thanks.")
print()

print("Best Regards,")
print(sender_name)

# 4. Consider the ferry in Problem 2. Assume it has only 50 tons of remaining capacity.
# Using comments, write an algorithm to check whether a new vehicle weighing a given number of tons can board the ferry.
# Use clear steps in your comments to outline the process.

# Step 1: (50 tons) Start with remaining capacity of the ferry
# Step 2: Figure out the weight of the new vehicle in tons
# Step 3: Compare the vehicle weight to the remaining capacity
# If the vehicles weight is less than or equal to 50 tons then the vehicle can board
# If the vehicles weight is more than 50 tons than the vehicle can not board
# Step 4: Output if the vehicle can board the ferry or not.
