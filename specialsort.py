def special_sort():
	s=[]
	i=0
	while i<5:
	
		s.append(int(input('type ints')))
		i +=1
	print s

	i=0
	minus=[]
	plus=[]

	while i<5:
		if s[i]<0:
			minus.append(s[i])
		elif s[i]>0:
			plus.append(s[i])
		i +=1
	i=0	
	while i<len(plus):
		minus.append(plus[i])
		i +=1
	
	print(minus)
