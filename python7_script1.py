#!/usr/bin/env python3
import re
import sys
file1=sys.argv[1]
with open(file1,"r") as file_nobody:
  for line in file_nobody: 
    for i in re.finditer(r"Nobody",line):
     find1=i.group(0)
     start1=i.start(0)
     end1=i.end(0)
     print(find1,start1,end1)

