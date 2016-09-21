#!/usr/bin/python
import sys
import re 


for line in sys.stdin:
    data = line.strip().split("\t")
    for string in data:
		x = re.findall(r'GET(.*?)HTTP',string)
		print "".join(x).replace('\n',' ')