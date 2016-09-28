## Test for taking in the input and setting up variables

#Imports
import math
import random
import numpy as np
import csv
import sys
import re
#from StringIO import StringIO


#arguements from input .csv file
script, inPut = sys.argv

#dataT = np.loadtxt(open(csvIN,"rb"),delimiter=",",skiprows=1)
ln = ""
lx = 0
ly = 0
counter = 0
fr = open(inPut, R)
for line in fr:
    #print line
    #if line contains "#":
        counter++
    #else
        if counter==0:
            #NO start header, skip
        elif counter==1:
            #if line contains "A":
                #A is active, set weight
            #elif line contains "B":
                #B is active, set weight
            #elif line contains "C":
                #C is active, set weight
            #...
            #elif line contains "Z":
                #Z is active, set weight
        elif counter == 2:
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
           #lx = x
           #ly = y
       elif counter == 4:
           #set inclusive contraints on items
       elif counter == 5:
           #set exclusive contraints on items
       elif counter == 6:
           #Set items to be in same bag
       elif counter == 7:
           #set items to never be in the same bag
       elif counter == 8:
           #set items and bags to be mutally inclusive
    
    f.closed

       




     





