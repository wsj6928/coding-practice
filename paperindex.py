def indexes():
	paper_list=raw_input('type each papers reference number:')
	a=paper_list.split(' ')
	a=[int(x) for x in a]
#h-index

	h_index=0
	i=0
	count=0
	
	for h_index in range(len(a)+1):
		for i in range(len(a)):
			if a[i]>=h_index:
				count +=1
		
		if count==h_index:
			break
		count=0
	print('h-index: %d' %(h_index))

#g-index 
	
	g_index=0
	i=0
	count=0

	a.sort()
	a.reverse()

	for g_index in range(len(a)+1):
		for i in range(1,len(a)+1):
			if sum(a[:i])>=g_index**2:
				count +=1
			
		if count<g_index:
			break
		count=0
	print('g-index: %d' %(g_index))
				

