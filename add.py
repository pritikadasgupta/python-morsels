#!/bin/python3

def add(m1,m2):
	'''accepts two lists-of-lists of numbers and 
	returns one list-of-lists with each of the 
	corresponding numbers in the two given 
	lists-of-lists added together'''
	mat3 = []
	for row1, row2 in zip(m1, m2):
		row = []
		for n,m in zip(row1, row2):
			row.append(n+m)
		mat3.append(row)
	return(mat3)