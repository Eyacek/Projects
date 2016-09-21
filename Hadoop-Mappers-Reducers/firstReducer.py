#!/usr/bin/python

import sys




# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

myDict = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    if thisKey not in myDict:
        myDict[thisKey] = float(thisSale)
    elif thisKey in myDict and myDict[thisKey] < float(thisSale):
        myDict[thisKey] = float(thisSale)
    else:
        continue 

for key,val in myDict.iteritems():
    print "{0}\t{1}".format(key, val)
    