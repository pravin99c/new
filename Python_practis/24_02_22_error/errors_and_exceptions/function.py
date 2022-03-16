# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("division by zero!")
#     else:
#         print("result is", result)
#     finally:
#         print("executing finally clause")

# for line in open("myfile.txt"):
#     print(line, end="")

# with open("myfile.txt") as f:
#     for line in f:
#         print(line, end="")


# amount = 10000

# if(amount > 2999):
#     print("You are eligible to purchase Dsa Self Paced")

# marks=100000
# a = marks / 0
# print(a)

a = [1, 2, 3]
try:
    print ("Second element = %d" %(a[1]))
    print ("Fourth element = %d" %(a[3]))
 
except:
    print ("An error occurred")