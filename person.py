# Daniel Ocean 
# CISW 24 LAB
# 10/15/17
# Program 4 

class Person:

	first_name = None
	last_name = None

	def __init__(self, first='NoFirstName', last='NoLastName'):
		self.first_name = first
		self.last_name = last

	def setFirstName(self, first):
		self.first_name = first

	def setLastName(self, last):
		self.last_name = last

	def getFirstName(self):
		return self.first_name

	def getLastName(self):
		return self.last_name

	def __repr__(self):
		return '[Person: %s %s]' % (self.first_name, self.last_name)

if __name__ == '__main__':
	print("constructed Person with defaults")
	print("NoFirstName NoLastName")
	
	



	