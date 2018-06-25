def binary():
	number=input('input number:')
	dimension=input('input dimension:')

	n=[]
	c=number

	while number!=0:
		b=number%dimension
		number=number/dimension
		n.append(b)
	n.reverse()
	n=[str(x) for x in n]
	m=""
	for x in n:
		m=m+x
	print m
