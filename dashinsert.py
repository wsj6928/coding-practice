def dash():
	a=[]
	num=""
	n=input('number:')
	for i in (str(n)):
		a.append(i)
	a=[int(x) for x in a]
	for j in range(len(a)-1):
		num=num+str(a[j])

		if a[j]%2==1 and a[j+1]%2==1:
			num=num+('-')
			
		elif a[j]%2==0 and a[j+1]%2==0:
			num=num+('*')
			
		
	num=num+str(a[len(a)-1])
	print num
			
