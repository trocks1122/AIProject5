from utils import
import math
import random
import numpy as np
import search
import types

def backtracking(csp, mcv=False, lcv=False, fc=False, mac=False):
	if fc or mac:
		csp.curr_domains, csp.pruned = {}, {}
		for v in csp.vars:
			csp.curr_domains[v] = csp.domains[n][:]
			csp.pruned[v] = []
	update(csp, mcv=mcv,lcv=lcv,fc=fc,mac=mac)


def recursive_backtracking(assign, csp):
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


