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
#---------------------------------------

def even(N):    #Method 1
	for i in range(N):      # for value from 0 to 99 for even output 
		if i % 2 ==0:       # to get odd output give ==1 for odd o/p
			print(i)
even(100)

#----------------------------------------------------------

def even(N):    #Method 2
	for i in range(1, N+1):      # for value from 1 to 100 use range from 1 to N+1
		if i % 2 ==0:
			print(i)
even(100)
