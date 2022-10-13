#!/usr/bin/env python3
import sys
number1=sys.argv[1]
number2=sys.argv[2]
for num in range(int(number1),int(number2)):
 if num%2!=0: 
   print(num)
