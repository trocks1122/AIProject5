import math
from functools import reduce

class Bag(object):
	def __init__(self, name, capacity):
		#a bag is an object wiith a name, max weight capacity, list of items and list of constraints
		self.name = name
		self.capacity = int(capacity) #convert to int
		self.items = []
		constraits = []

	def weight(self, weight, item):
		#gives weight of an item plus the rest of the bag
		return item.weight + weight

	def total_weight(self):
		#gives total weigt of bag
		total_weight = reduce(self.weight, self.items, 0)
		return total_weight


	def almost_full(self):#returns true if the bad is 90%-100% full
		weight = self.total_weight()
		almost_weight = math.floor(self.capacity*.9)
		if weight < almost_weight:
			return false
		else:
			return true



	def fits_in_bag(self, item):# return true if item will fit in bag
		weight = self.total_weight()
		if (item.weight + weight) <= self.capacity:
			return true
		else:
			return false

	



			