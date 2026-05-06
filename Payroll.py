def main():
	hrly_wage = 15.5
	hrs_worked = "20"	# Bug here
	salary = hrly_wage + hrs_worked	# Bug here
	print(f"Salary: ${salary}")

if _name_ == "_main_":
	main()