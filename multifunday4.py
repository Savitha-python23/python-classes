def mul(num, mul):
	for data in range(1, num + 1):  # Method 1
		print(data * mul)
mul(10,5)
#----------------------------------------------

def mul(num, m):
	value = []
	for data in range(1, num + 1): # Method 2 using append method
		value.append(data * m)
	return value
print(mul(10,5))

#----------------------------------------------
#List compression 

def mult(n, s):
	data = [d * s for d in range(1, n + 1)] #  simple method for multiplication
	return data 
print(mult(10,5))

#-----------------------------------------------


	
