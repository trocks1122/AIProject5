## Test for taking in the input and setting up variables

#Imports
import math
import random
import numpy as np
import csv
import sys
import re
from .Bag import Bag
from .item import Item
from .constraint import Constraint
from .csp import CSP
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


#create objects
bagsO = {}
itemsO = {}

for a in range items:
    name = items0[a]
    weight = itemsW[a]
    items[name] = Item(name, weight)

for b in range bags:     
    name = bags0[b]
    capacity = bagsC[b]
    bags[name] = Bag(name, capacity)

for c in bagsO:
    constraint = Constraint(Constraint.BAG_FIT_CON, bags=[bags[c]], min_items=fitLim[0], max_items=fitLim[1])
    bags[c].constraints.append(constraint)

for d in inclI:
    constraint = Constraint(Constraint.UC_IN_BAGS, items=[items[inclI[d]]], bags=inclB[d])
    items[inclI[d]].constraints.append(constraint)

for e in exclI:
    constraint = Constraint(Constraint.UC_NOT_IN_BAGS, items=[items[exclI[e]]], bags=exclB[e])
    items[exclI[e]].constraints.append(constraint)

for f in binEqI:
    itemA = binEqI[f][0]
    itemB = binEqI[f][1]
    constraint = Constraint(Constraint.BC_EQ, items=[items[item1], items[item2]])
    for g in [item1, item2]: 
        items[i].constraints.append(constraint)

for h in binEqI:
    itemA = binUnI[h][0]
    itemB = binUnI[h][1]
    constraint = Constraint(Constraint.BC_INEQ, items=[items[item1], items[item2]])
    for j in [item1, item2]: 
        items[j].constraints.append(constraint)

for k in mutInc:
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
solver = 
solution = solver.solve(csp)


#Output


