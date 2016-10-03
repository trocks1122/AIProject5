from .constraint import Constraint
import copy

class Solver(object):
    def order_domain(self, item, csp, potential_bags):
		bag_constraints = []
		items_potential_bags= potential_bags[item.name]

		for bag in items_potential_bags:
			count = 0
			for constraint in item.constraints:
				if (constraint.constraint_type >= Constraint.BC_EQ):
					neighbor = constraint.get_neighbor(item)
					item.bag = items_potential_bags[bag]
					items_potential_bags[bag].items.append(item)
					#number of invalid bags
					invalid_bags = self.num_invalid_bag(neighbor, potential_bags[neighbor.name])
					items_potential_bags[bag].items.remove(item)
					item.bag = None

					count += invalid_bags

			bag_constraints.append([csp.bags[bag], count])

		sorted(bag_constraints, key = lambda bag: bag[1])


		bags = [bag[0] for bag in bag_constraints]

		return bags

    def num_invalid_bag(self, item, potential_bags):
        count = 0
        for bag in potential_bags:
            item.bag = potential_bags[bag]
            potential_bags[bag].items.append(item)

            for constraint in item.constraints:
                if not constraint.validate():
                    count += 1
                    break
            potential_bags[bag].items.remove(item)
            item.bag = None
        return count

    def __get_num_constraints(self, csp, unassigned_items):
        num_constraints = {}
        for item_name in unassigned_items:
            count = 0
            for constraint in csp.items[item_name].constraints:
                if (constraint.constraint_type >= Constraint.BC_EQ):
                    for item in constraint.items:
                        if item.name != item_name in unassigned_items:
                            count += 1
            num_constraints[item_name] = count
        return num_constraints

    def is_complete(self, assignment, csp):
        return len(assignment) == len(csp.items)

    def test_all_bags(self, csp):
        for bag in csp.bags:
            condition1 = not csp.bags[bag].almost_full()
            condition2 = not csp.bags[bag].lower_limit()

            if condition1 or condition2:
                return False
        return True

    def select_unassigned_vars(self, assignment, csp, potential_bags):
        unassigned_items = {item_name: csp.items[item_name] for item_name in csp.items if item_name not in assignment}

        unassigned_item_names = list(unassigned_items.keys())
        min_item_name = unassigned_item_names[0]

        num_constraints = self.__get_num_constraints(csp, unassigned_items)

        for item_name in unassigned_item_names[1:]:
            num_bags_remaining = len(potential_bags[item_name])
            num_min_item = len(potential_bags[min_item_name])

            if num_bags_remaining < num_min_item:
                min_item_name = item_name
            elif num_bags_remaining == num_min_item:
                if num_constraints[item_name] >= num_constraints[min_item_name]:
                    min_item_name = item_name
        return csp.items[min_item_name]


    def consistent(self, bag, item, assignment, csp):
        if not bag.fits_in_bag(item):
            return False
        assigned_item_name = assignment.keys()
        for constraint in item.constraints:
            if Constraint.UC_IN_BAGS <= constraint.constraint_type <= Constraint.UC_NOT_IN_BAGS:
                item.bag = bag
                bag.items.append(item)
                if not constraint.validate():
                    bag.items.remove(item)
                    item.bag = None
                    return False
                item.bag = None
                bag.items.remove(item)

            elif Constraint.BC_EQ <= constraint.constraint_type<= Constraint.BC_INC:
                neighbor = constraint.get_neighbor(item)
                if neighbor.name in assigned_item_name:
                    item.bag = bag
                    bag.items.append(item)

                    for neighbor_bag_name in assignment[neighbor.name]:
                        neighbor.bag = csp.bags[neighbor_bag_name]
                        neighbor.bag.items.append(neighbor)
                        if not constraint.validate():
                            neighbor.bag.items.remove(neighbor)
                            bag.items.remove(item)
                            neighbor.bag = None
                            item.bag = None
                            return False
                        neighbor.bag.items.remove(neighbor)
                        neighbor.bag = None
                    bag.items.remove(item)
                    item.bag = None
        return True



    def backtrack(self, assignment, csp, potential_bags):
        if self.is_complete(assignment, csp):
            if self.test_all_bags(csp):
                return assignment
            else:
                return None

        new_potential_bags = potential_bags.copy()

        item = self.select_unassigned_vars(assignment, csp, new_potential_bags)
        for bag in self.order_domain(item, csp, new_potential_bags):
            if self.consistent(bag, item, assignment, csp):
                if item.name not in assignment:
                    assignment[item.name] = []

                assignment[item.name].append(bag.name)
                bag.items.append(item)

                inferences = self.inference(csp, item, bag, assignment, new_potential_bags)
                if inferences is not None:
                    result = self.backtrack(assignment, csp, new_potential_bags)
                    if result is not None:
                        bag.items.remove(item)
                        return result

                    for inference in inferences:
                        for value in inverences[inference]:
                            new_potential_bags[inference][value] = inferences[inference][value]

                bag.items.remove(item)
                assignment[item.name].remove(bag.name)

                if len(assignment[item.name]) == 0:
                    assignment.pop(item.name)
        return None


    def inference(self, csp, item, bag, assignment, potential_bags):
        return self.forward_checking(csp, item, bag, assignment, potential_bags)

    def forward_checking(self, csp, item, bag, assignment, potential_bags):
        unassigned_items = {item_name: csp.items[item_name] for item_name in csp.items if item_name in assignment}

        inferences = {}

        for constraint in item.constraints:
            if Constraint.BC_EQ <= constraint.constraint_type < Constraint.BC_INC:
                neighbor = constraint.get_neighbor(item)
                if neighbor.name in unassigned_items:
                    bag.items.append(item)
                    item.bag = bag 
                    invalid_bags = self.clean_neighbors(constraint, neighbor, potential_bags)
                    bag.items.remove(item)
                    item.bag = None

                    if invalid_bags is None:
                        return None
                    inferences[neighbor.name] = invalid_bags
        return inferences

    def clean_neighbors(self, constraint, item, potential_bags):
        invalid_bags = {}
        loop = potential_bags[item.name].copy()

        for bag in loop:
            item.bag = potential_bags[item.name][bag]
            if not constraint.validate():
                invalid_bags[bag] = potential_bags[item.name].pop(bag)
            item.bag = None
        if len(potential_bags[item.name]) == 0:
            return None

        return invalid_bags

    def solve(self, csp):
        potential_bags = {}
        for item in csp.items:
            potential_bags[item] = csp.bags.copy()

        back = self.backtrack({}, csp, potential_bags)

        result = {}
        for bag in csp.bags:
            result[bag] = []
        if back:
            for item in back:
                for bag in back[item]:
                    result[bag].append(item)
        else:
            return None
        return result

