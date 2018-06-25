def perf_num():
	list=[]
	n=input('number:')
	for i in range(1,n+1):
		for j in range(1,i):
			if i%j==0:
				list.append(j)
		if sum(list)==i:
			print i
		list=[]
