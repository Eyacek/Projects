#!/usr/bin/python

import sys 

prev = None 
counter = 1
for line in sys.stdin:
	data_mapped = line.strip()
	if prev == data_mapped:
		counter += 1
	else:
		print prev, "Hits: ", counter
		counter = 1 
		prev = data_mapped
		