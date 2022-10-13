#!/usr/bin/env python3

count=1000
total=1
while count != 1:
  print("count:", count)
  total*=count
  count-=1
print(f"Done,The total is {total}")
