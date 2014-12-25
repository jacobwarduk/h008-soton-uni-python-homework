#!/usr/bin/env python

# Importing modules
import math
import random


# Defining random division by 3 function
def rand_divis_3():
	while True:
		n = random.randint(0, 100)	# Generating random number between 0 and 100
		print n	# Printing number
		
		# If number is not divisible by 3 then pass
		if (n % 3 != 0 or n <= 3):
			pass
		else:
			return True
	
rand_divis_3()	# Executing function


print "\n"


# Definining dice function where x is number of sides and y is number of dice
def roll_dice(x, y):
	for i in range(y):
		num = random.randint(1, x)
		print num
	print "That's all!"
	
roll_dice(3, 2)	# Executing function
