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
A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = ([-1,'abcdefghijklmnopqrstuvwxyz'] for i in range(26))  
#follows this pattern:
#	[0]: Active/weight; -1 => inactive and should be discarded
#	[1]: add all possible box matches
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q , r, s, t, u, v, w, x,y,z = ([-1] for i in range(26))
#follows this pattern:
#	[0]: Active/capacity; -1 => inactive and should be discarded
#	[?]
rMin = 0
rMax = 0 #Range of inclusion from min to max

ln = ""
lx = 0
ly = 0
counter = 0
fr = open(inPut) 
lines = fr.readlines()

for i in range(len(lines)):
    ln = lines[i].rstrip('\n')
    ln = ln.replace(" ", "")
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
            if ln.find("A") != -1:
                A[0] = int(re.search(r'\d+', ln).group())
                #print A
            elif ln.find("B") != -1:
                B[0] = int(re.search(r'\d+', ln).group())
                #print B
            elif ln.find("C") != -1:
                C[0] = int(re.search(r'\d+', ln).group())
                #print C
            elif ln.find("D") != -1:
                D[0] = int(re.search(r'\d+', ln).group())
                #print D
            elif ln.find("E") != -1:
                E[0] = int(re.search(r'\d+', ln).group())
                #print E
            #...
            #elif line contains "Z":
                #Z is active, set weight
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

       




     





