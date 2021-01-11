#!/bin/python3

import collections

def count_words(s):
	# words = defaultdict(list)
	s_split = s.split()
	y=collections.Counter(s_split)
	return(y)
	# for i in range(length(s_split)):
		# my_dict[str(i)].append(s_split[i])
