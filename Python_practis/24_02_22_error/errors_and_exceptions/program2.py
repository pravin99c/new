# import sys

# # try:
# #     f = open('myfile.txt')
# #     s = f.readline()
# #     i = int(s.strip())
# #     print(s)
# # except OSError as err:
# #     print("OS error: {0}".format(err))
# # except ValueError:
# #     print("Could not convert data to an integer.")
# # except BaseException as err:
# #     print(f"Unexpected {err=}, {type(err)=}")
# #     raise

# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except OSError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()

# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print(type(inst))    # the exception instance
#     print(inst.args)     # arguments stored in .args
#     print(inst)          # __str__ allows args to be printed directly,
#                          # but may be overridden in exception subclasses
#     x, y = inst.args     # unpack args
#     print('x =', x)
#     print('y =', y)


def this_fails():
    x = 'hhghh'
    x=int(x)
try:
    this_fails()
except ValueError as err:
    print('Handling run-time error:', err)