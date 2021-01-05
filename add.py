#!/bin/python3

def add(*mats):
	mat3 = []
	for rows in zip(*mats):
		row=[]
		for values in zip(*rows):
			total = 0
			for n in values:
				total += n
			row.append(total)
		mat3.append(row)
	return(mat3)