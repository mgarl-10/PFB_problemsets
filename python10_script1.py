#!/usr/bin/env python3
import re
import sys
file1=sys.argv[1]
width=sys.argv[2]
#start=int(0)
#end=int(60)
def new_lines(dna,widt):
 list_dna=list(dna)
 start=int(0)
 end=int(widt)
 res=[]
 for line in dna:
  res.append(line.replace("\n",""))
 while dna[start:end]!='':
  print(dna[start:end])  
  start+=int(widt)
  end+=int(widt)
  
print(new_lines(file1,width))



