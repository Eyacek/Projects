#!/usr/bin/python
import sys
import re 


for line in sys.stdin:
    data = line.strip().split("\t")
    for string in data:
		x = re.findall(r'GET(.*?)HTTP',string)
		y = x[0]
		if y.startswith("http://www.the-associates.co.uk"):
			y = y[31:]
		if y.strip() == "/" or None:	
			continue 
		print y