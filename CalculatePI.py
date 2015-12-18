#  File: CalculatePI.py

#  Description: Calculates the Value of PI using random numbers

#  Student Name: Evan Yacek

#  Student UT EID: ety78

#  Course Name: CS 303E

#  Unique Number: 50475

#  Date Created: 10/1/2015

#  Date Last Modified: 10/3/2015






import math
import random

def  computePI(numThrows):
	
	circleCount = 0           #Keeps track of how many darts land in the circle
	
	for dart in range(numThrows):
	
		xPos = random.uniform (-1.0, 1.0)    #Generates random values for x and y
		yPos = random.uniform (-1.0, 1.0)
		
		
		if math.hypot(xPos, yPos) <= 1.0:    #Checks to see if falls in range of the circle, if so adds one.
			circleCount += 1
			
	return (4*circleCount) / numThrows       #Returns ratio of darts in circle to throws, the estimated Value of pi 
	
	
	
	
def main():

	lo = 100                                     #set Min
	hi = 100000000                               #ser Max

	print("Computation of PI using Random Numbers", end = '\n\n') #Print the header so that it is left justified and spaced from rest.
	
	while(lo < hi):                              #while loop through range lo-hi
	
		dartThrows = lo                          #Set the value of the dart throws
		pi = computePI(dartThrows)               # compute value of pi
		print("num = %d \t Calculated PI = %f   Difference = %+f" %(dartThrows, pi, pi - math.pi)) #%d holds the spot for the num integer, \t tabs, %f holds the spot for a float decimal, the plus is added for positive values
		lo = 10*lo                               # lo will increase by a factor of 10
	
	print( '\n',"Difference = Calculated PI - math.pi", sep = '') #\n to space, and sep = '' here will left justify
	
	
	
    
main()
	
	