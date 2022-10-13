#!/usr/bin/env python3
import sys
file1=sys.argv[1]
counted_line=0
counted_character=0

with open(file1,"r") as seq_read:
  for line in seq_read:
    line=line.rstrip()
    counted_line+=1
  print(f"The total number of lines in this file is {counted_line}")

with open(file1,"r") as seq_read:
  for line in seq_read:
    line=line.rstrip()
    char_count=len(line)
    counted_character+=char_count
  print(f"The total number of characters in this file is {counted_character}")
average_line_len=counted_character/counted_line
print(f"The average line length of this file is {average_line_len}")


