#!/usr/bin/env python3
import sys
file1=sys.argv[1]

seq_file_obj = open(file1,"r")
for line in seq_file_obj:
  line=line.rstrip()
  print(line)
seq_file_obj.close()

seq_file_obj=open(file1,"r")
for line in seq_file_obj:
  line=line.upper().rstrip()
  print(line)
seq_file_obj.close()

with open(file1,"r") as seq_file_obj, open("Python_06_uc.txt", "w") as seq_write:
  for line in seq_file_obj:
    line=line.upper().rstrip() 
    seq_write.write(line)

