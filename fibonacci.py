#!/usr/bin/env python


# Function to generate n numbers of fibonacci sequence
def fibonacci(n):	
	(x, y) = (0, 1)	# First two numbers to start off with
	i = 0	# Set counter to 0
	while i < n:
		print(y)	# Printing fibonacci number
		(x, y) = (y, x + y)	# Updating x as y and y as x + y
		i += 1	# Incrementing counter i++

fibonacci(20)	# Executing function


# Seemingly redundant second part of question sheet???
fib = list()
(x, y) = (0, 1)
i = 0
while i < 20:
	print(y)
	fib.append(y)
	(x, y) = (y, x + y)
	i += 1

print fib