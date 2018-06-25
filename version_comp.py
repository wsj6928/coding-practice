def version_comparing():
	a=raw_input('version a:')
	b=raw_input('version b:')

	aa=a.split('.')
	bb=b.split('.')

	aa=[int(x) for x in aa]
	bb=[int(x) for x in bb]

	for i in range(len(aa)):

		if aa[i]>bb[i]:
			print a,'>',b
			break
		elif aa[i]<bb[i]:
			print a,'<',b
			break
		
		
