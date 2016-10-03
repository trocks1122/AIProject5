from .item import Item

class Constraint(object):
    #Bag fit constraint
    BAG_FIT_CON =1

    BI_GOOD = 0
    BI_2_MUCH = -1
    BI_NOT_ENOUGH = 1

    #Unary constraints
    UC_IN_BAGS = 2
    UC_NOT_IN_BAGS = 3

    #Binary constraints
    BC_EQ = 4
    BC_IEQ = 5
    BC_INC = 6

    def __init__(self, constraint_type, min_items=-1, max_items=-1, items = [], bags = []:
    self.min_items = int(min_items)
    self.max_items = int(max_items)
    self.items = items
    self.bags = bags
    self.constraint_type = constraint_type

    def get_neighbor(self, me):
        for item in self.items:
            if item !=me:
                return item
        return None

    def bag_fit_limit(self):
        if self.constraint_type == self.BAG_FIT_CON:
            if self.min_items < 0 or self.max_items < 0:
                raise ValueError("ERROR: Fit limits must be positive integers")
            if len(self.bags[0].items) < self.min_items:
                return Constraint.BI_NOT_ENOUGH    
            elif len(self.bags[0].items) > self.min_items:
                return Constraint.BI_2_MUCH
            return Constraint.BI_GOOD

        return -2

    def validate(self):

        if self.constraint_type = self.UC_IN_BAGS:
            if len(self.items) < 1 or len(self.bags) < 1:
                raise ValueError("ERROR: Check your values for Unary Constraint - Item in bags")
            for bag in self.bags:
                if self.items[0].bag == bag:
                    return True
            return False            

        elif self.constraint_type == self.UC_NOT_IN_BAGS:
            if len(self.items) < 1 or len(self.bags) < 1:
                raise ValueError("ERROR: Check your values for Unary Constraint - Item not in bags")
            for bag in self.bags:
                cond = self.items[o] not in bag.items
                if not cond:
                    return False
            return True

        elif self.constraint_type == self.BC_EQ:
            if len(self.items) < 2:
                raise ValueError("ERROR: Check your values for Binary Constraint - Equal")
            return self.items[0].bag is self.items[1].bag

        elif self.constraint_type == self.BC_INEQ:
            if len(self.items) < 2:
                raise ValueError("ERROR: Check your values for Binary Constraint - InEqual")
            return self.items[0].bag is not self.items[1].bag

        elif self.constraint_type == self.BC_INC:
            if len(self.items) < 2 or len(self.bags) < 2:
                raise ValueError("ERROR: Check your values for Binary Constraint - Mutual Inclusive")
            both_in_condition = self.items[0].bag in self.bags and self.items[1].bag in self.bags
            both_not_in_condition = self.items[0].bag not in self.bags and self.items[1].bag not in self.bags 
            return both_in_condition or both_not_in_condition







