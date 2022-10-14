#!/usr/bin/env python3
import re
import sys
file1=sys.argv[1]
headers=0
#ids=re.findall(r("^>\w+\s?.*",line)
with open(file1,"r") as file_nobody:
  for line in file_nobody:
    for i in re.findall(r"^>\w+\s?.*",line):
      headers+=1
      
print(f"There are {headers} sequences in this file")



