# a=['mary','had','a','little','lamb']
# for i in range(len(a)):
#     print(i,a[i])

# for i in range(2,10):
#     for j in range(2,i):
#         if i%j==0:
#             print(i,'equals',j,'*',i//j)
#             break
#     else:
#         print(i,'is a prime number')
      
# n=int(input("Enter number : "))
# for i in range(1,n):
#     if i%2==0:
#         print(i,'Even number')
#     else:
#         print(i,'odd number')

# print(list(range(3,6)))
# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# pairs.sort(key=lambda pair:pair[1])
# print(pairs)
# l=[5,8,9,4,5]
# print(sorted(l))
# m=['g','f','o']
# print(sorted(m))
# m.sort()
# print(s)
# s=l.sort()
# print(type(l))
# print(l)

#Python if else in list comperhension

# def digitsum(n):
#     dsum=0
#     for i in str(n):
#         dsum+=int(i)
#     return  dsum
# list = [367,111,562,945,6726,873]
# newList = [digitsum(j) for j in list if j & 1]
# print(newList)


# python nested If statement

i=10
if i==10:
    if i<15:
        print('I is smaller than 15')
    if i<12:
        print('I is smaller than 12 too')
    else:
        print("I is greater than 15")