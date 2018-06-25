def selfnum():
	temp=[]
	notself=[]
	n=input('range:')
	for i in range(1,n+1):
		for j in (str(i)):
			temp.append(j)
		temp=[int(x) for x in temp]
		notself.append(sum(temp)+i)
		temp=[]
	notself=list(set(notself))
	self=range(1,n+1)
	for x in notself:
		if x<=n:
			self.remove(x)
	print self
	print sum(self)
