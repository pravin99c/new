# Sets
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # no value ripit

print('orange' in basket) # True And False
print('crabgrass' in basket)


# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a,b)              # unique letters in a
print(a - b)            # letters in a but not in b
print( a | b  )         # letters in a or b or both
print(a & b)            # letters in both a and b
print(a ^ b)            # letters in a or b but not both

#  list comprehensions
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)