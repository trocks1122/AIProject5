## Test for taking in the input and setting up variables

#Imports
import math
import random
import numpy as np
import csv
import sys
import re
#from StringIO import StringIO


#arguements from input  file
script, inPut = sys.argv

#Variables 
items = []
itemsW = []
bags = []
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
            items.append(ln[0])
            itemsW.append(int(re.search(r'\d+', ln).group()))
        elif counter == 2:
            #print "Counter = 2"
            ln = ln.replace(" ", "")
            bags.append(ln[0])
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
print items 
print itemsW 
print bags 
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
    name = items[a]
    weight = itemsW[a]
    itemsO[name] = Item(name, weight)

for b in range bags:     
    name = bags[b]
    capacity = bagsC[b]
    bagsO[name] = Bag(name, capacity)

for c in bags:
    constraint = Constraint(Constraint.BAG_FIT_LIMIT, bags=[bags[c]], min_items=fitLim[0], max_items=fitLim[1])
    bags[c].constraints.append(constraint)

for d in inclI:
    name = inclI[d]
    reqBags = inclB[d]
    constraint = Constraint(Constraint.UNARY_CONSTRAINT_IN_BAGS, item








