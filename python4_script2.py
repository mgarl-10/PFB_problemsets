#!/usr/bin/env python3

#when using = to make a new variable, the original variable also changes
my_list = ['a', 'bb', 'ccc']
list_copy = my_list
print(my_list)
list_copy.append('dd')
print(my_list)


#when using the .copy method the original variable remains unchanged
my_list2 = ['a', 'bb', 'ccc']
list_copy2 = my_list2.copy()
print(my_list2)
list_copy2.append('dd')
print(my_list2)
