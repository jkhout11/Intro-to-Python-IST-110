print("Welcome to Penn State World Campus")
print("")
#Prompt for their name.
first_name = input("Please, enter your first name: ")
#Prompt for their phone number.
phone_number = input("Please, enter your phone number: ")
#ID Creation using first letter of name and last 4 digits of number.
student_id = first_name[0] + phone_number[-4:]
#print ID
print("Your new student ID is: ", student_id)