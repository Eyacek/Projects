#!/usr/bin/python

import sys 
maxPath = None
prev = None 
counter = 1
maxCount = 0 
for line in sys.stdin:
	data_mapped = line.strip()
	if prev == data_mapped:
		counter += 1
	else:
		if maxCount < counter:
			maxPath = prev 
			maxCount = counter 
		
		counter = 1 
		prev = data_mapped
		
print maxPath , maxCount 