# class abc():
#     def add(self,A,B):
#         c=A+B
#         print(c)
#     def sub(self,A,B):
#         d=A-B
#         print(d)

# A1=abc()
# A1.add(7,5)
# A1.sub(7,5)



stack = []
 
# append() function to push
# element in the stack
stack.append('v')
stack.append('f')
stack.append('g')
 
print('Initial stack')
print(stack)
 
# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)
