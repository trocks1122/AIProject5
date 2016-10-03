class Item(object):
	def __init__(self, name, weight):
		#item has a name and weight, no bag but has potential bags and has constramits
		self.name = name
		self.weight = int(weight) #convert to int
		self.bag = None
		self.potential_bags = {}
		self.constraints = []

	def putInBag(self, bag):
		if self.bag:
			self.bag.items = [s for s in self.bag.items if s.name is not self.name]
			bag.items.append(self)
			self.bag = bag