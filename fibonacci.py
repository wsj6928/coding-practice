def evenf():
	fibo=[1,2]
	evenfibo=[]

	n=input('number:')

	i=0
	while fibo[i]+fibo[i+1]<n:
		fibo.append(fibo[i]+fibo[i+1])
		i +=1
	#print fibo
	
	for i in fibo:
		if i%2==0:
			evenfibo.append(i)
	#print evenfibo

	print sum(evenfibo)
	
