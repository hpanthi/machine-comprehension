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


