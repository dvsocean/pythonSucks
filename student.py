# Daniel Ocean 
# CISW 24 LAB
# 10/15/17
# Program 4 

from person import *

class Student(Person):
	
	courses = []

	def __init__(self, first='NoFirstName', last='NoLastName', course=''):
		Person.__init__(self, first, last)
		self.courses = [course]

	def setMainCourse(self, course):
		self.courses.insert(0, course)

	def getCourses(self):
		return self.courses

	def addCourse(self, course):
		self.courses.append(course)

	def dropCourse(self, course):
		if course in self.courses:
			self.courses.remove(course)
			print("Removed " + course)
		else:
			print("Sorry " + course + " could not be found")
		
	def __repr__(self):
		return '[Student: %s %s]' % (Person.__repr__(self), (self.courses))














