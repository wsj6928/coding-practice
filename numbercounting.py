def number_counting():
	a=[]
	n=input('from 1 to~:')
	for i in range(1,n+1):
		for x in (str(i)):
			a.append(x)
	for j in range(0,10):
		b=a.count('%d'%(j))
		print ('%d:'%(j)),b
