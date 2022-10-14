#!/usr/bin/env python3
#R is A or G
#Y is T or C
import re
import sys
file1=sys.argv[1]
headers=0
#ids=re.findall(r("^>\w+\s?.*",line)
with open(file1,"r") as file2:
  for line in file2:
    for i in re.findall(r"[AG]AATT[TC]",line):
      headers+=1
      it=i
      print(it)
print(f"There are {headers} sites in this sequence")



