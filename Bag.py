import math
from .constraint import Constraint
from functools import reduce

class Bag(object):

	def __init__(self, name, capacity):
		#a bag is an object wiith a name, max weight capacity, list of items and list of constraints
		self.name = name
		self.capacity = int(capacity) #convert to int
		self.items = []
		self.constraints = []

	def __weight(self, weight, item):
		#gives weight of an item plus the rest of the bag
		return item.weight + weight

	def __total_weight(self):
		#gives total weigt of bag
		total_weight = reduce(self.weight, self.items, 0)
		return total_weight

	def almost_full(self):#returns true if the bad is 90%-100% full
		weight = self.__total_weight()
		almost_weight = math.floor(self.capacity*.9)
		if weight <= almost_weight:
			return False
		else:
			return True

	def fits_in_bag(self, item):# return true if item will fit in bag
		weight = self.__total_weight()
		if item.weight + weight <= self.capacity:
            if not self.__fit_upper_limit(item):
                return False
			return True
		else:
			return False

    def __fit_upper_limit(self, item):
        for constraint in self.constraints:
            self.items.append(item)
            result = constraint.bag_fit_limit()
            self.items.remove(item)
            if result == Constraint.BI_2_MUCH:
                return False
        return True

    def fit_lower_limit(self):
        for constraint in self.constraints:
            result = constraint.bag_fit_limit()
            if result == Constraint.BI_NOT_ENOUGH:
                return False
        return True

    def __eq__(self, other):
        if isinstance(other, Bag):
            return self.name == other.name
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result








 



			
