#!/usr/bin/env python

# Declaring new class Stones()
class Stones:
	
# Defining constructor method
	def __init__(self):
		
		self.stones = 100	# Setting number of stones to 100
		self.pile = []	# Declaring pile list for stones
		
		self.playerOne = raw_input("Player 1, please enter your name: ")	# Getting player one's name
		self.playerTwo = raw_input("Player 2, please enter your name: ")	# Getting player two's name
		 
	
# Defining method to check number of stones left in pile
	def checkStones(self):
		if self.stones <= 0:
			return True
		else:
			return False
	
	
# Defining method to print number of stones left in pile
	def printStones(self, stones):
		print "\n\n%d stones left in pile." % (stones)	# Printing number of stones left in pile
		
		# Should be able to use a one-liner here, but can't work it out!!! :@
		self.pile = ["o" for i in range(0, (stones))]	# List comprehension to make stones for printing out
		self.pile = [self.pile[i:i+10] for i in range(0, len(self.pile), 10)]	# List comprehension to split into groups of 10
		
		# Printing out the pile of stones
		for i in self.pile:
			print " ".join(i)
			
	
# Defining method to remove stones from pile
	def removeStones(self, n):
		
		# Trying to convert user input to an integer
		try:
			n = int(n)
		except (ValueError):
			print "\nPlease enter a valid number..."	# Telling user they didn't enter a valid number
			return False

		# If users choice of number of stones is valid
		if n <= 5 and n >= 1 and not n > self.stones:
			self.stones -= n	# Remove stones from pile
			return True
		else:
			print "\nInvalid number of stones to remove, please try again..."	# Telling user they chose an invalid number of stones
			return False


# Defining method to take turn
	def takeTurn(self, player):
			
		self.printStones(self.stones)	# Printing number of stones left in pile
		
		# While user chooses their number of stones
		while True:
			# If user removes a valid number of stones
			if self.removeStones(raw_input("\n" + player + ", please remove your stones: ")) == True:
				# If user removed last stones
				if self.checkStones() == True:
					print "\033[1m" + "\n *** %s is the winner! *** \n" % (player)	# Print winner in bold!
					print "\033[0m"	# Returning to normal font weight
					return False
				break


# Defining method to play the game	
	def playGame(self):
		
		print "\nWelcome %s and %s to the game of stones. \nIn front of you sits a pile of %d stones. \nYou may each take turns in removing 1 to 5 stones, the person to remove the last stone wins. \nLet the game begin!" % (self.playerOne, self.playerTwo, self.stones)	# Printing welcome message and instructions
		
		# Players taking turns until takeTurn() returns False
		while True:
			if self.takeTurn(self.playerOne) == False:
				break
			if self.takeTurn(self.playerTwo) == False:
				break


		
game = Stones()	# Instantiating new Stones() object as game

game.playGame()	# Starting a new Stones game


