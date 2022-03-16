# num1=[1,2,3,4,5]
# num2=[6,7,8,9,10]
# result=map(lambda x,y:x+y,num1,num2)
# print(list(result))

# List of strings
l = ['sat', 'bat', 'cat', 'mat']
  
# map() can listify the list of strings individually
test = list(map(list, l))
print(test)