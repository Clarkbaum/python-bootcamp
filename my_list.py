import os
import statistics

class List:
	def __init__(self):
		self.my_list = []


	def push(self, value):
		self.my_list.append(value)


	def pop(self):
		return self.my_list.pop()


print(statistics.mean([1,2,3,5,6,7,5,4]))
