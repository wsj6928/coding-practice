def dn():
	number=str(input('type number:'))
	i=0
	digit_num=[]
	for i in range(10):
		count=number.count('%d' %(i))
		digit_num.append(count)
		if count>1:
			print 'False at %d' %(i)

	if digit_num.count(0)+digit_num.count(1)==len(digit_num):
		print 'True'
		
	else:
		print 'False'
