def rotation():
	a=raw_input('type list:')
	b=a.split(' ')	
	n=int(b[0])
	b.remove(b[0])	
	m=n%len(b)
	str=""
	

	for x in range(len(b)-m,len(b)):
		str=str+b[x]+" "
	for x in range(0,len(b)-m):
		str=str+b[x]+" "

	print str
		
