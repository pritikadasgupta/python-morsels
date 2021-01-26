#!/bin/python3

def parse_ranges(string):
	string1 = string.split(",")
	for range_num in string1:
		range_num = range_num.split('->')[0]
		try:
			yield int(range_num)
		except ValueError:
			first_num, second_num = [int(x) for x in range_num.split('-')]
			for num in range(first_num,second_num+1):
				yield num

