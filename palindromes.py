#!/usr/bin/env python

# Function to test if word is a palindrome	
def palindrome(word):
	if (word == word[::-1]):
		return True
	else:
		return False



user_input = raw_input("Enter a word: ")	# Receiving user input and assigning to user_input variable

# Running palindrome() function and printing output
if (palindrome(user_input.lower())):
	print "Congrats, '%s' is a palindrome!" % (user_input)
else:
	print "Sorry, '%s' is not a palindrome :(" % (user_input)