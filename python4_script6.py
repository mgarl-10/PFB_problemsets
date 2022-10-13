#!/usr/bin/env python3

new_list=[101,2,15,22,95,33,2,27,72,15,52]
even_numbers=[]
odd_numbers=[]
sorted_list=sorted(new_list)
for number in sorted_list:
  if number %2==0:
    even_numbers.append(number)
  else:
    odd_numbers.append(number)
sum_even=sum(even_numbers)
sum_odd=sum(odd_numbers)
print(f"Sum of even numbers is {sum_even}")
print(f"Sum of odd numbers is {sum_odd}")

