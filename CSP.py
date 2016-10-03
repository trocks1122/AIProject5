from utils import
import math
import random
import numpy as np
import search
import types


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

	def fits_in_bag(self, item):
		weight = self.total_weight()
		if item.weight + weight <= self.capacity:
			






class CSP(search.problem):
	def __init__(self, vars, domains, neighbors, constraints):
		vars = vars or domains.keys()
		update(slef, vars=vars, domains=domains, neighbors=neighbors, initial={}, curr_domains=None, pruned=None, nassigns=0)

	def assign(self, var, val assignment):
		self.nassign += 1
		assignment[var] = 1 
		if self.curr_domains:
			if self.fc:
				self.forward_check(var, val, assignment)
			if self.mac:
				Arc_Consistent(self, [(xk, var) for xk in self.neighbors[var]])

	def unassign(self, var, assignment):
		if var in assignment:
			if self.curr_domains:
				self.curr_domains[var] = self.domains[var][:]
			del assignment[var]

	def conflict(self, var, val, assignment):
		testVal = assignment.get

	def forwardCheck(self, var, val, assignment):
		#performs forward checking on given assignment
		if self.curr_domains:
			for (i, h) in self.pruned[var]:
				self.curr_domains[i].append(h)
			self.pruned[var] = []
			for i in self.neighbors[var]:
				if i not in assignment:
					if h in self.curr_domains[i][:]:
						if not self.constraint(var, val, i, h):
							self.curr_domains[i].remove[h]
							self.pruned[var].append((i, h))

	def succ(self, assignment):
		if len(assignment) == len(self.vars):
			return []
		else:
			car = find_if(lambda v: v not in assignment, self.vars)
			result = []
			for val in self.domains[var]:
				if self.nconflicts(self, var, val, assignment) == 0:
					a = assignment.cope; a[var] = val
					result.append(((var, val), a))
			return result
	

	def goal(self, assignment):
		return (len(assignment) == len(self.vars) and every(lambda var: self.nconflicts(var, assignment[var], assignment) == 0, self.vars))
	
	def conflicted_vars(self, currrent):
		return [var for var in self.vars if self.nconflicts(var, current[var], current) > 0]


def backtracking(csp, mcv=False, lcv=False, fc=False, mac=False):
	if fc or mac:
		csp.curr_domains, csp.pruned = {}, {}
		for v in csp.vars:
			csp.curr_domains[v] = csp.domains[n][:]
			csp.pruned[v] = []
	update(csp, mcv=mcv,lcv=lcv,fc=fc,mac=mac)


def recursive_backtracking(assignment, csp):
	if len(assign) == len(csp.vars):
		return assign
	var = select_unassigned_variable(assignment, csp)
	for val in order_domain_values(var, assignment, csp):
		if csp.fc or csp.nconflicts(var, val, assignment) == 0:
			csp.assign(var, val, assignment)
			result = recursive_backtracking(assignment, csp)
			if result is not None:
				return result
			csp.unassign(var, assignment)
	return None

def select_unassigned_variable(assignment, csp):
	if csp.mcv:
		unassigned = [v for v in vsp.vars if v not in assignment]
		return argmin_random_tie(unassigned, lambda var: -num_legal_values(csp, var, assignment))
	else:
		for v in csp.vars:
			if v not in assignment:
				return v
def order_domain_values(var, assignment, csp):
	if csp.curr_domains:
		domain = csp.curr_domains[var]
	else:
		domain = csp.domain[var][:]
	if csp.lcv:
		key = lambda val: csp.nconflicts(var, val, assignment)
		domain.sort(lambda (x,y): cmp(key(x), key(y)))

	while domain:
		yield domain.pop()

def num_good_vals(csp, var, assignment):
	if csp.curr_domains:
		return len(csp.curr_domains[var])
	else:
		return count_if(lambda val: csp.nconflicts(var, val,assignment) == 0, csp.domains[var])


def Arc_Consistent(csp, queue=None):
	#from figure 6.3
	if queue == None:
		queue = [(i,h) for i in csp.vars for h in csp.neighbors[i]]
	while queue:
		(i, j) = queue.pop()
		if remove_bad_vals(csp, i, j):
			for h in csp.neighbors[i]:
				queue.append((h, i))

def remove_bad_vals(csp, i, j):
	removed = False
	for x in csp.curr_domains[i][:]:
		if every(lambda y: not csp.constraints(i, x, j, y), csp.curr_domains[j]):
			csp.curr_domains[i].remove(x)
			removed = true
	return removed
