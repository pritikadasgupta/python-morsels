#!/bin/python3

def parse_ranges(string):
	string1 = string.split(",")
	for range_num in string1:
		first_num, second_num = [int(x) for x in range_num.split('-')]
		for num in range(first_num,second_num+1):
			yield num

