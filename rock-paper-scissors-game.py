#/usr/bin/env python

hands = ["rock", "paper", "scissors"]	# List of valid hands

# Dictionary of hands beats hands
beats = {
	"rock" : "scissors", 
	"scissors" : "paper", 
	"paper" : "rock"
}

# Determining whether a hand is valid
def validHand(hand):
	if (hand not in hands):
		return True
	else:
		return False

# Getting player one's hand
while True:
	playerOne = raw_input("Player 1: ").lower()
	if (validHand(playerOne)):
		print "Please enter a valid hand..."
	else:
		break

# Getting player two's hand
while True:		
	playerTwo = raw_input("Player 2: ").lower()
	if (validHand(playerTwo)):
		print "Please enter a valid hand..."
	else:
		break

# Looping to beats to determine the winner
for beat in beats:
	if (playerOne == beat):
		print "Player 1 selected %s, Player 2 selected %s, so Player 1 wins!" % (playerOne, playerTwo)
		break
	else:
		print "Player 1 selected %s, Player 2 selected %s, so Player 2 wins!" % (playerOne, playerTwo)
		break
		