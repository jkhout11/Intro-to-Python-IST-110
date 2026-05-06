# 1) Donation Center
print("Donation Center")
shirts = int(input("How many shirts? "))
pants = int(input("How many pants? "))
jackets = int(input("How many jackets? "))

money = shirts * 3 + pants * 5 + jackets * 10

print("You earned $%d" % money)


# 2) Report Card
print("Report Card")
class1 = input("Input class: ")
grade1 = float(input("Input grade: "))

class2 = input("Input class: ")
grade2 = float(input("Input grade: "))

print("%-10s %.2f" % (class1, grade1))
print("%-10s %.2f" % (class2, grade2))


# 3) String slicing
print("String Slicing")
s = input("Enter 'pythonisgreat': ")

print("word 1", s[0:6])
print("word 2", s[6:8])
print("word 3", s[8:13])


# 4) Meters conversion
print("Meters Conversion")
m = float(input("Enter meters: "))

METERS_PER_MILE = 1609.34
METERS_PER_FOOT = 0.3048
METERS_PER_INCH = 0.0254

miles = m / METERS_PER_MILE
feet = m / METERS_PER_FOOT
inches = m / METERS_PER_INCH

print("Miles: %.2f" % miles)
print("Feet: %.2f" % feet)
print("Inches: %.2f" % inches)