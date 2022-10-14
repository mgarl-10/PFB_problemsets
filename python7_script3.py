#!/usr/bin/env python3
import re
import sys
file1=sys.argv[1]
headers=0
ids=r"^>(\w+)"
with open(file1,"r") as file2:
  for line in file2:
    for i in re.findall(ids,line):
      headers+=1
print(f"There are {headers} sequences in this file")
