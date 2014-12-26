#!/usr/bin/env python

data = "Name,Gender,Age\nSandy,Female,13\nIwan,Male,21\nGary,Male,44\nLolita,Female,30\nSarah,Female,43\nJohn,Male,50"

f = open("people.csv", "w")

f.write(data)

f.close()