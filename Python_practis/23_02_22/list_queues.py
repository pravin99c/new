# Using Lists as Queues

from collections import deque

list1 = deque(["Eric", "John", "Michael"])
list1.append('Terry')
list1.append("Graham") 
print(list1)
list1.popleft()#deleted first value
print(list1)


#  ********------List Comprehensions-----*******

squares = []

for x in range(10):                 # 17 to 28 all  in one
    squares.append(x**2)            

print(squares)


list2 = list(map(lambda x:x**2, range(10)))
print(list2)


list3 = [x**2 for x in range(10)]
print(list3)

# A list comprehension
# [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
#fist 
list4=[]
for i in [1,2,3]:
    for j in [3,1,4]:
        if j != i:
            list4.append((i,j))
print(list4)

# secound 
print([(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y])

# create a new list with the values doubled
vec = [-4, -2, 0, 2, 4]

n=[x*2 for x in vec]
print(n)

# filter the list to exclude negative numbers
s=[x for x in vec if x>=0]
print(s)

# apply a function to all the elements
all=[abs(x) for x in vec] # positive
print(all)

# string

# strip minig __ deleted
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
str1=[weapon.strip() for weapon in freshfruit]
print(str1)

# number
# the tuple must be parenthesized, otherwise an error is raised
num=[(x, x**2) for x in range(6)]
print(num)

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
vec1=[num for elem in vec for num in elem]
print(vec1)

# math import function
from math import pi
print([str(round(pi, i)) for i in range(1, 6)])