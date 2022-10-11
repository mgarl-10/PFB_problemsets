#!/usr/bin/env python3
random_number=50

if random_number > 0: 
  if random_number <50:
    print("The number is positive and less than 50")
    if random_number %2==0:
      print("It is an even number that is smaller than 50")
  elif random_number==50:
    print("The number is 50")  
  else:
    if random_number %3==0:
      print("It is larger than 50 and divisible by 3") 
else:
  print("It is a negative number")
