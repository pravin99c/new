# while True print('Hello world')H == Invalid syntex

# print(10 * (1/0)) #integer division or modulo by zero


# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")
#     except (RuntimeError, TypeError, NameError):
#         pass

# except Exception as e:

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [C, D, B]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")