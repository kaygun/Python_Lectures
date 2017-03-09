#!/usr/bin/python

## Backend

import csv

FILE = "/home/kaygun/local/lib/TR.txt"

data = open(FILE,'r')
dataReader = csv.reader(data, delimiter="\t")
raw = [x for x in dataReader]
data.close()

reverseLookup = {x[1].strip(" "): map(lambda x: x.strip(" \t"), [x[2],x[3],x[5]]) for x in raw}

def getDistrict(zip):
    y = map(lambda x: x.strip(" "), reverseLookup[zip])
    print "{:<12} {:<12} {:<12}".format(y[1],y[2],y[0])

lookupData = {}

for x in raw:
    try:
        temp1 = lookupData[x[3]]
        try:
            temp2 = temp1[x[5]]
            temp2.update({x[2]: x[1]})
        except:
            temp1.update({x[5]: {x[2]: x[1]}})
    except:
        lookupData.update({x[3]: {x[5]: {x[2]: x[1]}}})

def getZipCode(a,b):
    if b == "":
       for j in lookupData[a].keys():
           print "{:<12}".format(j)
           for i in lookupData[a][j].keys():
               print " "*12,
               print "{:<11} \t {:<5}".format(i, lookupData[a][j][i])
    else:
         for i in lookupData[a][b].keys():
             print "{:<11} \t {:<5}".format(i, lookupData[a][b][i])


## Front end

import sys

n = len(sys.argv)

if n < 3:
   print "error"
   exit
elif sys.argv[1] == "reverse":
   getDistrict(sys.argv[2])
elif sys.argv[1] == "zip":
   if n == 3:
      getZipCode(sys.argv[2],"")
   else:
      getZipCode(sys.argv[2],sys.argv[3])
