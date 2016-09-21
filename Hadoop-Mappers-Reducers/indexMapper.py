#!/usr/bin/python
import sys
import re 
import csv


reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)


import sys
import re 
import csv

reader = csv.reader(sys.stdin, delimiter='\t')



for line in reader:

	
	
	body = line[4].strip().split()
	id = line[0]
	for word in body:
		word = re.sub(r'<(.*?)>', " ", word) #Removes Html tags
		word = re.sub('[-{}\<>=)(!??.:;#/@,+%"$^]' , ' ' ,word) #Removes symbols
		word = word.lower()
		print word.strip() , id 
			
