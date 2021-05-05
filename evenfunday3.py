s = "SAVITHA"
a = list(enumerate(s)) # Method 1
print(a)

for k in enumerate(s): # Method 2
	print(k)


def idx(s):
	for data in range(len(s)): # Method 3
		print(data,s[data])
idx(s)


