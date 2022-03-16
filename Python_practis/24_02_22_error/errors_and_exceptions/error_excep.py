# try:
#     # Some Code.... 

# except:
#     # optional block
#     # Handling of exception (if required)

# else:
#     # execute if no exception

# finally:
#     # Some code .....(always executed)



try:
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    c = a/b
    print("The answer of a divide by b:", c)
except ValueError:
    print("Entered value is wrong")
except ZeroDivisionError:
    print("Can't divide by zero")