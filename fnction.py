def hyper():
	print("HELLO")
# hyper()


# Single return

def up():
	s = "SAVITHA"
	return s[::-1]
# print(up())

def d2():
	data = up()
	return data

print(d2())

#-------------------------------------------------------

# Multiple return

def evvi():
	say = "Hello"
	bye = "bye"
	return say, bye

def call():
	s, v = evvi()
	return s, v
print(call())

# ----------------------------------------------------------------

def do_something(name):
	return "Hello", name
print(do_something(1))

#-------------------------------------------------

def jio():
	s = {1, 2, 3}
	u = {1, 3, 4}
	return(s.intersection(u))
print(jio())












