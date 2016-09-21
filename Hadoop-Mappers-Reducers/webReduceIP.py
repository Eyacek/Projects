#!/usr/bin/python

import sys 

wordcount = {}
prev = None 
count = 1
for word in sys.stdin:
	word = str(word).strip()
	if word not in wordcount:
		wordcount[word] = 1
	else:
		wordcount[word] += 1

x = wordcount['10.99.99.186']
print x 