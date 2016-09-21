#!/usr/bin/python
import sys
import re 


for line in sys.stdin:
    data = line.strip().split("\t")
    for string in data:
		ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', string )

		print ip[0] 