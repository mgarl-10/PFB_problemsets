#!/usr/bin/env python3
#R is A or G
#Y is T or C
import re
import sys
file1=sys.argv[1]
headers=0
with open(file1,"r") as file2:
  for line in file2:
    for i in re.finditer(r"([AG]AATT[TC])",line):
     find1=i.group(0)
     start1=i.start(0)
     end1=i.end(0)  
     print(find1,start1,end1,sep="\t") 
     #find1=i.group(0)
     #start1=i.start(0)
     #end1=i.end(0)
     #print(find1,start1,end1)


