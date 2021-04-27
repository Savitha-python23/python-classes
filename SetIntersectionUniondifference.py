# union method 1


# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.union(y)
# print(z)  

# union method 2

l1 = {1, 2, 3, 4, 5}
l2 = {1, 6, 7, 8, 9, 10}
l3 = l1.union(l2)
print(l3)

# intersection method 1
a = {5, 4, 3, 2, 1}
b = {1, 2, 3, 6, 7}
print(a.intersection(b))

# intersection method 2
a = {5, 4, 3, 2, 1}
b = {1, 2, 3, 6, 7}
c = {1, 2}
print(a.intersection(b,c))

# difference
A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}
print (A.difference(B))
print (B.difference(A))

x = {"hello", 9, 10, "hi"}
y = {9, "hi", 6,  "bye"}
print(x.difference(y))
print(y.difference(x))











