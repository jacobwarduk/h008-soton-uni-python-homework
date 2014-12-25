#!/usr/bin/env python

# Phonebook Dictionary
phoneBook = {
	"Tom" : "0545345345367", 
	"John" : "0764345323434", 
	"Sandy" : "0235452342465", 
	"Ewan" : "0656875345234", 
	"Andy" : "0673423123454", 
	"Rebecca" : "0656875345234", 
	"Vicky" : "0456740034344", 
	"Gary" : "0656875345234"
}

countryCode = "0044-"	# Country code to prepend to phone numbers

# For each number in the phonebook
for number in phoneBook:
	phoneBook[number] = countryCode + phoneBook[number]	# Prepend with country code
	
print phoneBook	# Printing phone book

names = []	# Declaring names list

# For each name in phone book
for name in phoneBook:
	names.append(name)	# Append to names list

names.sort()	# Sort names list

print names	# Print names list


