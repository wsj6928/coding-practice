def multisum(a):
	sum=0
	for x in range(1,a):
		if x%3==0 or x%5==0:
			sum=sum+x
	return sum
