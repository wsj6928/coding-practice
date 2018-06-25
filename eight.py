def eight():

	n=input('range:')
	a=range(1,n+1)
	temp=[]

	for i in a:
		for j in (str(i)):
			temp.append(j)
	print temp.count('8')
	
