import os
import statistics

class List:
	def __init__(self):
		self.my_list = []


	def push(self, value):
		self.my_list.append(value)


	def pop(self):
		return self.my_list.pop()


