# def fun(s=100, a=200): # key value key value # will work
	# return s,a
# fun()

#--------------------------
# def fun(s=100,a): # key value parameter error wont work
	# return s,a
# fun()
#-----------------------------
# def fun(a,s=100): # parameter key value will work if we give value 1 when we call fun(1)
	# return a,s
# fun(1)

#-------------------------------

def func(Num=100):  # function override 
	print(Num)
func(200)
