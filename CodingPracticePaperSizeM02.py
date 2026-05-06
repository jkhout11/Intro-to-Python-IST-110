#Constants mm per inch
mm_per_inch = 25.4

#Constant paper size
width_inches = 8.5
height_inches = 11

#Conversions from inches to millimeters
width_millimeters = mm_per_inch * width_inches
height_millimeters = mm_per_inch * height_inches

#Printed Results
print("Letter-size paper converted from inches to millimeters are:")
print("Width", width_millimeters, "mm")
print("Height", height_millimeters, "mm")