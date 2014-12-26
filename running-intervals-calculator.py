#!/usr/bin/env python

import csv	# Importing csv module

# Declaring variables
distance = float()
time = float()
calories = int()

f = "RunningIntervals.csv"	# Assigning csv file

# Trying to open CSV file
try:
	run = csv.reader(open(f, "r").readlines()[1::2])	# Opening every other line from CSV for reading
except (IOError):
	print "Unable to open file %s " % (csvFile)	# Unable to open file
	exit()	# Exiting

# Calculating total distance and time
for row in run:
	distance += float(row[2])	# Incrementing distance with next value
	time += float(row[1])	# Incrementing time with next value
	calories += int(row[3])	# Incrementing calories with next value

pace = (distance / time)	# Calculating the pace

# Printing out all the stats!
print "Total distance: %f" % (distance)
print "Average pace: %f" % (pace)
print "Calories burnt: %d " % (calories)