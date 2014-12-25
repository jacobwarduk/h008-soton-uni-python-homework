#!/usr/bin/env python

import calendar
from datetime import date
from time import strptime

# Function to validate all user dob input
def dobTest(x, y):
	
	# If user inputs year
	if y == "year":
		if len(x) == 4 and not int(x) > date.today().year:	# Year length must be 4 digits and be in the past
			return True
		else:
			return False
	
	# If user inputs a month
	if y == "month":
		for n in calendar.month_name:	# Checking to see if user inputted month is in calendar
			if x == n:
				return True
		else:
			return False
	
	# If user inputs day
	if y == "day":
		validDays = calendar.monthrange(int(dobYear), strptime(dobMonth[0:3], "%b").tm_mon)	# Getting valid number of days for specified month/year from the calendar
		if int(x) > 0 and int(x) <= validDays[1]:	# Checking to see if user inputted day is valid
			return True
		else:
			return False


firstName = raw_input("Enter your first name: ").title()	# Receiving user input for first name and capitalising first letters
lastName = raw_input("Enter your last name: ").title()	# Receiving user input for last name and capitalising first letters

print "Enter your date of birth: "

while True:
	dobYear = raw_input("Year? ")	# Receiving user input for year of birth
	if dobTest(dobYear, "year") == True:	# Validating user input
		break
	else:
		print "Please enter a valid year, e.g. 1985 ..."

while True:
	dobMonth = raw_input("Month? ").capitalize()	# Receiving user input for month of birth and capitalising first letter
	if dobTest(dobMonth, "month") == True: 	# Validating user input
		break
	else:
		print "Please enter a valid month, e.g. February ..."

while True:
	dobDay = raw_input("Day? ")	# Receiving user input for day of birth
	if dobTest(dobDay, "day") == True:	# Validating user input
		break
	else:
		print "Please enter a valid day, e.g. 23 ..."

print "%s %s was born on %s %s, %s" %(firstName, lastName, dobMonth, dobDay, dobYear)	# Printing message to screen!






