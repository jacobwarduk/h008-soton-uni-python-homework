#!/usr/bin/env python

# Importing modules
import random

def get_unsorted_list(amount_of_numbers):
	unsorted_list = list()
	for i in range(1, amount_of_numbers):
		unsorted_list.append(random.randint(1,10))
	return unsorted_list



def bubble_sort(unsorted_list):
	swapped = True
	while swapped == True:
		swapped = False
		for i in range(0, len(unsorted_list) - 1):
			if unsorted_list[i] > unsorted_list[i + 1]:
				swapped = True
				temp = unsorted_list[i]
				unsorted_list[i] = unsorted_list[i + 1]
				unsorted_list[i + 1] = temp
		
			i += 1
	return unsorted_list


unsorted_list = get_unsorted_list(10)

print unsorted_list

sorted_list = bubble_sort(unsorted_list)

print sorted_list