# try:
#     x = input()
#     print ('Try using KeyboardInterrupt')
# except KeyboardInterrupt:
#     print ('KeyboardInterrupt exception is caught')
# finally:
#     x = input()


# def get_size(text):
#     while True:
#         try:
#             i = int(input(text))
#             if i==10:
#                 break
#             elif i >= 0 and i<24:
#                 continue
#         except:
#             pass
#     return i

# a = get_size("Input: ")


# class Error(Exception):
#     """Base class for other exceptions"""
#     pass

# class ValueTooSmallError(Error):
#     """Raised when the input value is small"""
#     pass

# class ValueTooLargeError(Error):
#     """Raised when the input value is large"""
#     pass

# while(True):
#     try:
#         num = int(input("Enter any value in 10 to 50 range: "))
#         if num < 10:
#             raise ValueTooSmallError
#         elif num > 50:
#             raise ValueTooLargeError
#         break
#     except ValueTooSmallError:
#             print("Value is below range..try again")

#     except ValueTooLargeError:
#             print("value out of range...try again")

# print("Great! value in correct range.")


# heights = {'John': 175, 'Jane': 150, 'Jim': 155, 'Matt': 170}

# tall = {key:value for (key, value) in heights.items() if value >= 170}

# print(tall)