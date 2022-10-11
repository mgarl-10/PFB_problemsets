#!/usr/bin/env python3
import sys
random_number=sys.argv[1]

if int(random_number) > 0: 
  if int(random_number) <50:
    print(random_number + " is positive and less than 50")
    if int(random_number) %2==0:
      print(random_number + " is an even number that is smaller than 50")
    else:
      print(random_number + " is an odd number that is smaller than 50")
  elif int(random_number)==50:
    print(random_number + " is 50")  
  else:
    if int(random_number) %3==0:
      print(random_number + " is larger than 50 and divisible by 3") 
    else:
      print(random_number + " is larger than 50 and indivisible by 3")
else:
  print(random_number + " is a negative number")
