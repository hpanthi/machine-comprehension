import numpy as np
import itertools

def context(f):
	data=[]
	cont=[]
	with open(f,'r',encoding="utf8") as train:
		for l in train:
			num,line=tuple(l.split(" ",1))	#splits the line into line number and sentence
			if num=="1":			#if line number is 1, then start a new context
				cont=[]	
			#either the sentence is a q/a sentence or it is a normal context sentence			
			if "\t" in line:
				q,a,support_id=tuple(line.split("\t"))
				data.append((tuple(zip(*context))+sent2seq(q)+sent2seq(a)+([int(sup) for sup in support_id.split()],)))
			else:
				cont.append(sent2seq(line[:-1]))
	return data

def final(data):
	f_data=[]	
	for cont_q_a_sup in data:	
		cont_vs, cont_ws, q_vs, q_ws, a_vs, a_ws, sup = cont_q_a_sup
		# finds the total length of the contexts
		lengths = itertools.accumulate( len(cvec) for cvec in cont_vs )
		cont_vec = np.concatenate(cont_vs)
		cont_words = sum(cont_ws,[])
		# marks the beginning of new sentences
		st_ends = np.array(list(lengths))
		f_data.append((cont_vec, st_ends, q_vs, sup, cont_words, cont_q_a_sup, a_vs, a_ws))
	return np.array(f_data)
		
