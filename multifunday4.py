def mul(num, mul):
	for data in range(1, num + 1):  # Method 1
		print(data * mul)
mul(10,5)

def mul(num, m):
	value = []
	for data in range(1, num + 1):
		value.append(data * m)
	return value
print(mul(10,5))


	
