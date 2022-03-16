
# def fun(a):
#     if a < 4:
#         b = a/(a-3)
#     print("Value of b = ", b)

# try:
#     fun(3)
#     fun(5)
# except ZeroDivisionError:
#     print("ZeroDivisionError Occurred and Handled")
# except NameError:
#     print("NameError Occurred and Handled")

def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)

AbyB(2,3)
AbyB(3,3)
