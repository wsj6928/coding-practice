def printing_oxs():
	a='o'
	b='x'
	n=input('type number:')
	for i in range(n):
		print (a*(n-(i+1)))+(b*(i+1))
