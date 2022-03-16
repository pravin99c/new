# Data Structures

list=['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
list2=[5,6,4,7,8,9,2]
list.append(1)# list end value add
print(list)

list.extend(list2)# one list to add secound list add 
print(list)

list.insert(2,'pravin')# index(2) per value add 
print(list)

list2.remove(5) # single value remove 
print(list2)

list.pop()# list last value delete
print(list)

list2.clear()# all value delete 
print(list2)

print(list.index('banana',5))# value ni index find
# print(list)

# list.sort()# not supported between instances of 'int' and 'str'
# print(list)

# list.reverse()# not supported between instances of 'int' and 'str'
# print(list)

list2=list.copy()# copy method
print(list2)
list.pop()
list.pop()
print(list)
del(list[8:])# delet Start index to end index
print(list)


list.sort()# sorted only string and sorted only number ect.
print(list)

list.reverse()# reverse only string and reverse only number ect.
print(list)

c=list.count('banana') # count to value
print(c)
