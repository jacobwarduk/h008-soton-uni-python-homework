#!/usr/bin/env python

# Importing modules
import turtle
import Tkinter
import time
import random
import math

# Declaring new class Turtle()
class Turtle:


	# Defining constructor method
	def __init__(self):

		# Getting width and height of turtle window
		self.screenWidth = turtle.window_width()
		self.screenHeight = turtle.window_height()

		self.wait = 3	# Time to wait before turtle window closes


	# Defining drawShape methpd with number of sides (s) and length (l) as arguments
	def drawShape(self, s, l):
		angle = 360 / s	# Calculating the angle to turn the turtle

		# For the number of sides
		for i in range(0, s):
			turtle.down()	# Put the pen down
			turtle.forward(l)	# Move the turtle forward (l)
			turtle.right(angle)	# Turn the turtle angle (angle)

		time.sleep(self.wait)	# turtle.exitonclick() doesn't seem to work (Error: object has no attribute 'exitonclick') so I've just put a sleep in there
		turtle.clear()	# Clearing the screen


	# Defining drawSpiral method with number of increments (j) as argument, degrees to turn (d) and when to lift pen up (u)
	def drawSpiral(self, j, d, u):

		# For the number of increments
		for i in range(0, j):
			# If the angle is equal to when we want to lift the pen
			if i == u:
				turtle.up() # Lift the pen up
			else:
				turtle.down() # Put the pen down

			turtle.forward(i)	# Move the turtle forward (i)
			turtle.right(d)	# Turn the turtle angle (d)

			j += j	# Incrementing

		time.sleep(self.wait)	# turtle.exitonclick() doesn't seem to work (Error: object has no attribute 'exitonclick') so I've just put a sleep in there
		turtle.clear()	# Clearing the screen


professorChaos = Turtle()	# Instantiating new Turtle() object as professorChaos (RIP)


professorChaos.drawShape(4, 50)	# Drawing a square with 50px sides

professorChaos.drawShape(5, 50)	# Drawing a pentagon with 50px sides

professorChaos.drawShape(6, 50)	# Drawing a hexagon with 50px sides

professorChaos.drawShape(7, 50)	# Drawing a heptagon with 50px sides

professorChaos.drawShape(8, 50)	# Drawing an octogon with 50px sides

professorChaos.drawSpiral(50, 20, 37)	# Drawing the spiral, with the pen up at 37
