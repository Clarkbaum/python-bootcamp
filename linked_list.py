class LinkedList:
	def __init__(self, val):
		self.val = val
		self.head = None
		self.next = None

	def add(self, val):
		new_node = LinkedList(val)
		current = self
		if self.head == None:
			self.head = self
			self.next = new_node
		else:
			while current.next != None:
				current = current.next
		
		current.next = new_node

	def contains(self, val):
		output = False
		current = self
		while current.next != None:
			if current.val == val:
				output = True
			current = current.next

		return output

	def delete(self, val):
		previous = None
		current = self
		while current.next != None:
			if current.val == val:
				previous.next = current.next
			previous = current
			current = current.next
			
	def len(self):
		count = 1
		current = self
		while current.next != None:
			count += 1
			current = current.next


		return count


linkedList = LinkedList(10)
print(linkedList.val)
linkedList.add(15)
linkedList.add(20)
linkedList.add(25)
linkedList.add(30)
print(linkedList.contains(15))
linkedList.delete(15)
print(linkedList.contains(15))
print(linkedList.len())

