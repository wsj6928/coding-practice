def ones():
	a=range(0,10001)
	b=[]
	for x in a:
		if x%2!=0 and x%5!=0:
			b.append(x)
	print b
	
