#!/usr/bin/env python

# Dictionary of words to exclude as PigLatin
excludeDict = ["affray", "airplay", "airway", "aisleway", "allay", "alleyway", "alway", "antigay", "anyway", "archway", "areaway", "array", "ashtray", "assay", "astray", "away", "ay", "embay", "entranceway", "entryway", "essay", "estray", "everyday", "everyway", "expressway", "immunoassay", "inlay", "interlay", "interplay", "intraday", "ofay", "oilway", "okay", "orfray", "outlay", "outplay", "outpray", "outstay", "overlay", "overpay", "overplay", "overstay", "underlay", "underpay", "underplay", "underway", "unlay", "unsay"]

# Function to check if valid word entered
def validWord(word):
	# If is a real word entered
	if (len(original) > 0 and original.isalpha()):
		return True
	else:
		return False

# Function to check if word starts with a vowel
def startsWithVowel(word):
	first = word[0] # Get the first letter of the word
	
	# If the first letter is a vowel - maybe quicker to place vowels in list and perform not in ???
	if ((first == "a") or (first == "e") or (first == "i") or (first == "o") or (first == "u")):
		return True
	else:
		return False

# Function to check if word is in PigLatin
def isPigLatin(word):
	# If word starts with a vowel and ends in "ay"
	if (word[-2:] == "ay" and startsWithVowel(word) and word not in excludeDict):
		return True
	else:
		return False

# Function to translate to PigLatin
def transToPig(word):
	pyg = 'ay'  # Declaring and assigning pyg variable

	# If word is valid and starts with a vowel
	if (startsWithVowel(word) and validWord(word)):
		new_word = word + pyg   # Append word with pyg variable
		return new_word  # Print out piglatin word

	# Else the first letter is a consonant
	else:
		new_word = word[1:] + word[0] + pyg # Slice remainder of word after first letter, concatenate with first letter of word and pyg variable
		return new_word  # Print out piglatin word

# Function to translate to English
def transToEng(word):
	# If word is valid piglatin word	
	if (isPigLatin(word)):
		new_word = word[-3] + word[0:-3]
		return new_word
	else:
		return False

# Looping until valid word is entered
while True:
	original = raw_input("Enter a word: ").lower() # Recieving users word
	
	if (validWord(original) == True):
		break
	else: print "Please enter a valid word..."

# If word is PigLatin translate to English, else translate to PigLatin
if (isPigLatin(original)):
	print transToEng(original)
else:
	print transToPig(original)
	