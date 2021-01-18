#!/bin/python3

def tail(seq,n):
	if(n<=0):
		return([])
	else:
		seq1 = iter(seq)
		seq_ = list(seq1)
		if((n<=len(seq_)) & (n>0)):
			n_ = len(seq_)-n
			new_seq = []
			for (i) in range(n_,len(seq_)): 
				new_seq.append(seq_[i])
			return(new_seq)
		else:
			return(seq_)
