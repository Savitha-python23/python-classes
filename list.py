# l = list()

# print(dir(l))

# Append

# l = [1, 2, 3]
# a = 10
# l.append(a)
# print(l)
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# l1.extend(l2)
# print(l1)
for x in l2: l1.append(x)
print(l1)