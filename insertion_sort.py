def insertion_sort():
	a=raw_input('type:')
	a=a.split(' ')
	b=[]
	print a
	for i in range(1,len(a)):
		for j in range(0,i):
			print a[i],'i'
			print a[j],'j'
			if a[j]>a[i]:
				c=a[i]
				a.remove(a[i])
				a.insert(j,c)
				break
			print a
		
