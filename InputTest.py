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
ly = 0
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
        print ln
        if counter==0:
            print "Counter = 0"
            #NO start header, skip
        elif counter==1:
            print "Counter = 1"
            ln = ln.replace(" ", "")
            items.append(ln[0])
            itemsW.append(int(re.search(r'\d+', ln).group()))
        elif counter == 2:
            print "Counter = 2"
            #if line contains "a":
                #a is active, set weight
            #elif line contains "b":
                #b is active, set weight
            #elif line contains "c":
                #c is active, set weight
            #...
            #elif line contains "z":
                #z is active, set weight     
        elif counter == 3:
            print "Counter = 3"
            #lx = x
            #ly = y
        elif counter == 4:
            print "Counter = 4"
            #set inclusive contraints on items
        elif counter == 5:
            print "Counter = 5"
            #set exclusive contraints on items
        elif counter == 6:
            print "Counter = 6"
            #Set items to be in same bag
        elif counter == 7:
            print "Counter = 7"
            #set items to never be in the same bag
        elif counter == 8:
            print "Counter = 8"
            #set items and bags to be mutally inclusive

fr.closed

       
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



     





