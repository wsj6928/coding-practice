def names():
	name=raw_input('type')
#1
	name.split(',')
	print("starting a:%d \nstarting b: %d" %(name.count("a"),name.count("b")))
#2
	print(name.count("lee"))
#3
	name2=list(set(name))
#4
	print(name2.sort())



