def disassemble():
	n=input('till:')
	a=range(10,n+1)
	a=[str(x) for x in a]
	
	disect=[]
	multiples=[]

	for j in range(n+1-10):
		
		for i in (str(a[j])):
			
			disect.append(i)
			
			disect=[int(x) for x in disect]
		#print disect
			
		c=1
		for x in range(len(disect)):
			c=c*disect[x]
		
		multiples.append(c)	
		disect=[]

	#print multiples
	print sum(multiples)

