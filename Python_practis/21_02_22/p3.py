# for x in range(1, 11):
#      print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
for x in range(1,11):
     print(repr(x).rjust(2),repr(x*x).rjust(3),repr(x*x*x).rjust(4))
# import math
# print('The value of pi is approximately %5.3f.' % math.pi)
# print('12'.zfill(5))
# # file open
# f = open('workfile', 'w')
# with open('workfile') as f:
#     read_data = f.read()
# f.closed
# f.close()
# print(f.read())
