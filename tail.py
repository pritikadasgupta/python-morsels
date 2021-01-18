#!/bin/python3

def tail(seq,n):
	seq = list(seq)
	if(n <=len(seq) and n !=0):
		n_ = len(seq)-n
		new_seq = []
		for (i) in range(n_,len(seq)): new_seq.append(seq[i])
		return(new_seq)
	else:
		return(seq)
