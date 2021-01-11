#!/bin/python3

import re
import string

def toLower(ch):
	if (ord(ch) <= ord('Z')):
		return chr(ord(ch) + ord('a') - ord('A'))
	else:
		return ch

def count_words(s):
	# list1 = re.compile("[\w']+").findall(s) #also works
	list1 = "".join((c if c.isalnum() or c=="'" else ' ') for c in s ).split(' ')
	list1 = list(filter(None, list1))

	list2 = []
	for i in range(0,len(list1)):
		decap = []
		for j in range(0,len(list1[i])):
			ch = list1[i][j]
			if(j == 0):
				lowered = toLower(ch)
				decap.append(lowered)
			else:
				decap.append(ch)
		n1 = "".join(decap)
		list2.append(n1)
	s2 = " ".join(list2)
	mydict = {}
	for n in list2:
		if n not in mydict.keys():
			pattern = re.compile(r'\b{}\b'.format(n), re.I)
			word_count = len(pattern.findall(s2))
			mydict[n] = word_count
	return(mydict)

