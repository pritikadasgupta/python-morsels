#!/bin/python3

def add(*mats):
	mat3 = []
	for rows in zip(*mats):
		row=[]
		for values in zip(*rows):
			row.append(sum(values))
		mat3.append(row)
	return(mat3)