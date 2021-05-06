def sqr(square):
	l = []
	for data in square:
		l.append(data * data)#--- Method 1
	print(l)
sqr([1,2,3,4])
#-------------------------------

def sqre(a):
	data = [d * d for d in a] # ----- list comprehension method 2
	print(data)
sqre([1,2,3,4])

#--------------------------------------------

def sqt(element):
	return element * element
data = list(map(sqt, [1,2,3,4])) #-------- method 3 using map
print(data)
