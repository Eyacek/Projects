#!/usr/bin/python
import sys
import re 
import csv 


prevWord = None
nodes = []



for line in sys.stdin:
	data_mapped = line.strip().split(' ')
	if len(data_mapped) != 2 or data_mapped[1] == "id":
		# Something has gone wrong. Skip this line.
		continue

	currentWord , node_id = data_mapped
	

	
	
	if prevWord and prevWord != currentWord:
		print prevWord, "\t", sorted(nodes), "\t", len(nodes)
		prevWord = currentWord;
		nodes = []

	prevWord = currentWord
	nodes.append(int(node_id))

if prevWord != None:
	print prevWord, "\t", sorted(nodes), "\t", len(nodes)
