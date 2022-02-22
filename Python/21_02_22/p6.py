# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case _:
#             return "Something's wrong with the internet"
from nis import match
from sys import flags

flag = False
match (100, 200):
    case (100, 300):  # Mismatch: 200 != 300
       print('Case 1')
    case (100, 200) if flag:  # Successful match, but guard fails
       print('Case 2')
    case (100, y):  # Matches and binds y to 200
       print(f'Case 3, y: {y}')
    case _:  # Pattern not attempted
       print('Case 4, I match anything!')