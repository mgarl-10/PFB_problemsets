#!/usr/bin/env python3
#problem1
fav_dict={'book':'I contain multitudes','song':'Arctic Monkeys-Mardy Bum','tree':'maple'}
#problem2
print(fav_dict['book'])
#problem 3
fav_thing='book'
print(fav_dict[fav_thing])
#problem4
print(fav_dict['tree'])
#problem5
fav_dict['organism']='bacteria'
print(fav_dict)
fav_thing='organism'
print(fav_dict[fav_thing])
#problem6
for thing in fav_dict:
  print(thing)
choice = input("Choose one from above:")
if choice in fav_dict:
   print(fav_dict[choice])
#problem7
fav_dict["organism"]='beetles'
#problem8
fav_thing='food'
fav_thing=input("Mention one of your favorite things:")
print(sports)
#problem 9
for thing in fav_dict:
  things=fav_dict[thing]
  print(thing,things)

 

