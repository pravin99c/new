# try:
#     k = 5//2
# except ZeroDivisionError:
#     print("Can't divide by zero")
# else:
#     print(k)
# finally:
#     print('This is always executed')
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print ("An exception")
    raise