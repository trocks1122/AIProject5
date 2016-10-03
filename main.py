#Project 5
#Alex Ruggiero and Trevor Rocks



#Imports
import math
import random
import numpy as np
import sys
import re
import os.path
from classFiles.Bag import Bag
from classFiles.item import Item
from classFiles.constraint import Constraint
from classFiles.CSP import CSP
from classFiles.solver import Solver
#from StringIO import StringIO


#arguements from input  file
script, inPut = sys.argv

#Variables 
items0 = []
itemsW = []
bags0 = []
bagsC = []
fitLim = [] #Range of inclusion from min to max
inclI = []
inclB = []
exclI = []
exclB = []
binEqI = []
binUnI = []
mutInc = []

bags = {}
items = {}

ln = ""
lx = 0
ly = 10
counter = 0
fr = open(inPut) 
lines = fr.readlines()

for i in range(len(lines)):
    ln = lines[i].rstrip('\n')
    #print ln
    if ln.find("#") != -1:
        #print "This is comment" + ln
        counter+= 1
    
    else:
        
        if counter==0:
            #print "Counter = 0"
            print ""
            #NO start header, skip
        elif counter==1:
            #print "Counter = 1"
            ln = ln.replace(" ", "")
            items0.append(ln[0])
            itemsW.append(int(re.search(r'\d+', ln).group()))
        elif counter == 2:
            #print "Counter = 2"
            ln = ln.replace(" ", "")
            bags0.append(ln[0])
            bagsC.append(int(re.search(r'\d+', ln).group()))   
 
        elif counter == 3:
            #print "Counter = 3"
            fitLim = [int(n) for n in ln.split()]

        elif counter == 4: 
            #print "Counter = 4"
            temp = ln[1:]
            inclB.append([str(n) for n in temp.split()])
            ln = ln.replace(" ", "")
            inclI.append([ln[0]])
            
        elif counter == 5:
            #print "Counter = 5"
            temp = ln[1:]
            exclB.append([str(n) for n in temp.split()])
            ln = ln.replace(" ", "")
            exclI.append([ln[0]])
            
        elif counter == 6:
            #print "Counter = 6"
            binEqI.append([str(n) for n in ln.split()])

        elif counter == 7:
            #print "Counter = 7"
            binUnI.append([str(n) for n in ln.split()])

        elif counter == 8:
            #print "Counter = 8"
            mutInc.append([str(n) for n in ln.split()])

fr.closed

"""
print "Inputs:"       
print items0 
print itemsW 
print bags0 
print bagsC 
print fitLim
print inclI 
print inclB 
print exclI 
print exclB 
print binEqI
print binUnI
print mutInc
"""

for a in xrange(0,len(items0)):
    name = items0[a]
    weight = itemsW[a]
    items[name] = Item(name, weight)

for b in xrange(0,len(bags0)):     
    name = bags0[b]
    capacity = bagsC[b]
    bags[name] = Bag(name, capacity)

for c in bags:
    constraint = Constraint(
        Constraint.BAG_FIT_CON, bags=[bags[c]], 
        min_items=fitLim[0], max_items=fitLim[1])
    bags[c].constraints.append(constraint)

for d in xrange(0, len(inclI)):
    name = inclI[d][0]
    req_bags = []
    for m in xrange(0, len(inclB[d])):
        req_bags.append(bags[inclB[d][m]])
    constraint = Constraint(Constraint.UC_IN_BAGS, items=[items[name]], bags=req_bags)
    items[name].constraints.append(constraint)

for e in xrange(0, len(exclI)):
    name = exclI[e][0]
    rej_bags = []
    for n in xrange(0, len(exclB[e])):
        rej_bags.append(bags[exclB[e][n]])   
    constraint = Constraint(Constraint.UC_NOT_IN_BAGS, items=[items[name]], bags=rej_bags)
    items[name].constraints.append(constraint)

for f in xrange(0, len(binEqI)):
    itemA = binEqI[f][0]
    itemB = binEqI[f][1]
    constraint = Constraint(Constraint.BC_EQ, items=[items[itemA], items[itemB]])
    for g in [itemA, itemB]: 
        items[g].constraints.append(constraint)

for h in xrange(0, len(binEqI)):
    itemA = binUnI[h][0]
    itemB = binUnI[h][1]
    constraint = Constraint(Constraint.BC_INEQ, items=[items[itemA], items[itemB]])
    for j in [itemA, itemB]: 
        items[j].constraints.append(constraint)

for k in xrange(0, len(mutInc)):
    itemA = mutInc[k][0]
    itemB = mutInc[k][1]
    bag1 = mutInc[k][2]
    bag2 = mutInc[k][3]
    constraint = Constraint(Constraint.BC_INC, items=[
items[itemA], items[itemB]], bags=[bags[bag1], bags[bag2]])
    items[itemA].constraints.append(constraint)
    items[itemB].constraints.append(constraint)


#CSP and solve
csp = CSP(items, bags)
solver = Solver()
solution = solver.solve(csp)


#Output
print "CONCLUSION:  "
print " "
if solution is not None:
    keys = list(solution.keys())
    keys.sort()
    for bag in keys:
        total_w = sum(items[x].weight for x in solution[bag])
        print(bag + " " + " ".join(solution[bag]))
        print("number of items: " + str(len(solution[bag])))
        print("total wieght " + str(total_w) + "/" + str(bags[bag].capacity))
        print("wasted capacity: " + str(bags[bag].capacity - total_w))
else:
    print("No such assignment is possible")




