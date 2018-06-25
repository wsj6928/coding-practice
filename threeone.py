def threeone():
	ran=raw_input('range:')
	ran=ran.split(' ')
	ran=[int(x) for x in ran]
	r=range(ran[0],ran[1]+1)
	
	cycle=[]
	cyclelength=[]
	for i in r:
		n=i
		while not n==1:
			cycle.append(n)
			if n%2==0:
				n=n/2			
			else:
				n=(n*3)+1
		cycle.append(1)
		#print cycle
		cyclelength.append(len(cycle))
		cycle=[]
	print max(cyclelength)
			
