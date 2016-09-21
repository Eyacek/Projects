#!/usr/bin/python


import sys

dayCount = 0
daySalesTotal = 0 
prevDay = None 

for line in sys.stdin:


	line = line.strip().split("\t")
	if len(line) != 2:
		continue 
		
	curDay = line[0]
	sales = float(line[1])
	
	if prevDay and prevDay != curDay:
		
		print prevDay , "Mean Sales: " , daySalesTotal / dayCount
		dayCount = 0 
		daySalesTotal = 0
		prevDay = curDay
	
	
	prevDay = curDay
	dayCount += 1
	daySalesTotal += sales 
	
		
if prevDay != None:
	print prevDay, "Mean Sales: ", daySalesTotal / dayCount
	