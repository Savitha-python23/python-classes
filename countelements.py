import collections

# print(dir(collections))
# l = ["a", "a", "b", "c", "d", "d"]
# print(collections.Counter(l))
# print(help(collections.Counter))
l = ["a", "a", "b", "c", "d", "d"]
d = {}
for data in l:
	if data in d:
		d[data] = d[data] + 1
	else:

		d[data] = 1
print(d)


