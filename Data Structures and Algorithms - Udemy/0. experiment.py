class Test:
	def __init__(self):
		self.run = True

obj1 = Test()
obj2 = obj1
obj2.run = False
print('1', obj1.run)
print('2', obj2.run)
