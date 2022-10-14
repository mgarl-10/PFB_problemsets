#!/usr/bin/env python3
import re
import sys
file1=sys.argv[1]
with open(file1,"r") as file_nobody,open("Leo.txt","w") as seq_write:
  for line in file_nobody:
    new_file=re.sub(r'Nobody','Leo',line) 
    print(new_file)
    seq_write.write(new_file + "\n")



