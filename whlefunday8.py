# i = 1
# while i < 6:  # while loop
	# print(i)
	# i += 1

#---------------------------------

# Generate Random Number:

import random
def fun(run=False):
counter = 1
while counter < 7:
	user = int(input("Enter a number: "))
	r = random.randrange(1,11)
	if user == r:
		print("You guess the correct number")
		break
	else:
		counter += 1
	ask = "Your chances are met would you like to continue"
	ask_input = input("Type yes or no: ")
	if ask_input == "yes":
		def  fun2():
			data = fun()
			return data
		print(fun2())
	else:
		print("Thanks for playing")
		



	
		
		
		
	




