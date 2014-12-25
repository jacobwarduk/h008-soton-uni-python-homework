#!/usr/bin/env python

# Function to combine two lists into a dictionary
def combine_lists(k, v):
	persons = dict(zip(k, v))	# Zipping key/value pairs into dictionary
	return persons

# Function to return people of a particular age
def people(age):	
	age_list = filter(lambda x: x[1] == age, persons.items())	# Filtering dictionary values for age into tuple
	age_names = [age_list[i][0] for i in range(len(age_list))]	# Using list comprehension to build list of names from tuple
	return age_names

names = ["Alice", "Bob", "Cathy", "Dan", "Ed", "Frank", "Gary", "Helen", "Irene", "Jack", "Kelly", "Larry"]  
ages = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

persons = combine_lists(names, ages)
print persons

peoples = people(20)
print peoples

# Test cases from worksheet
print "Dan" in people(18) and "Cathy" in people(18)  
print "Ed" in people(19) and "Helen" in people(19) and "Irene" in people(19) and "Jack" in people(19) and "Larry" in people(19)  
print "Alice" in people(20) and "Frank" in people(20) and "Gary" in people(20)  
print people(21) == ["Bob"]  
print people(22) == ["Kelly"]  
print people(23) == []
