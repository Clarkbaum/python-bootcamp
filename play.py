class Person:
	def __init__(self, name):
		self.name = name
	def talk(self):
		print(f"hi im {self.name}")

person = Person("bob")
person.talk()


