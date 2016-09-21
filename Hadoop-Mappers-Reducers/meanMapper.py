#!/usr/bin/python
from datetime import datetime

import sys


for line in sys.stdin:


	line = line.strip().split("\t")
	sales = float(line[4])
	
	date = line[0]
	weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
	if weekday == 6:
		print "Sunday" , "\t" , sales
	if weekday == 5:
		print "Saturday", "\t" , sales
	if weekday == 4:
		print "Friday" ,"\t",  sales
	if weekday == 3:
		print "Thursday" ,"\t", sales
	if weekday == 2:
		print "Wednesday" ,"\t", sales
	if weekday == 1:
		print "Tuesday" ,"\t", sales
	if weekday == 0:
		print "Monday" , "\t" , sales