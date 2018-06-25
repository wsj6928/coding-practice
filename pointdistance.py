def points():
	i=0
	s=[]
	while i<7:
		s.append(int(input('points:')))
		i=i+1
		print s
	s.sort()
	print s
	i=0
	min=0
	dd=[]
	ss=abs(s[i]-s[i+1])
	min=ss
	print ss
	while i<6:
		ss=abs(s[i]-s[i+1])
		
		
		if ss<min:
			dd[i]=[s[i],s[i+1]]
			min=ss
		elif ss==min:
			dd.append([s[i],s[i+1])
		i= i+1
print(dd)
