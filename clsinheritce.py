class Employee:
	def __init__(self, first, last, email):
		self.first = first
		self.last = last
		self.email = email

	def printname(self):
		print(self.first,self.last,self.email)

a = Employee("Leo", 'A', 	'LeoSavi2322@gmail.com')
a.printname()

class Developer(Employee):
	def __init__(self, first, last, email, prog_lang):
		super().__init__(first, last, email)
		self.prog_lang = prog_lang
		
d1 = Developer("Leo", 'A', 	'LeoSavi2322@gmail.com', 'Python')
print(d1.prog_lang)
	    



















































