#!/bin/python3

import re
import string

def toLower(ch):
	if (ord(ch) <= ord('Z')):
		return chr(ord(ch) + ord('a') - ord('A'))
	else:
		return ch

def count_words(s):
	list1 = list(filter(None, re.compile("[\w']+").findall(s)))
	list2 = []
	for word_i in list1:
		decap = []
		for index_j,char_j in enumerate(word_i):
			if(index_j == 0):
				decap.append(toLower(char_j))
			else:
				decap.append(char_j)
		list2.append("".join(decap))
	s2 = " ".join(list2)
	mydict = {}
	for n in list2:
		if n not in mydict.keys():
			pattern = re.compile(r'\b{}\b'.format(n), re.I)
			mydict[n] = len(pattern.findall(s2))
	return(mydict)

