import random


class Users():
    def __init__(self,username,mobile_no,address, opening_balance):
        self.username=username
        self.mobile_no=mobile_no
        self.address=address
        self.account_no = random.randrange(1,999999999999)
        self.balance = opening_balance
        print(self.account_no)
    def __str__(self):
        return f'{self.username}\n{self.mobile_no}\n{self.address}\n{self.account_no}\nBalance: ${self.balance:.2f}\n'
class User_manager(Users):
    def __init__(self):
        self.users_list = []
        print("Succussfully creat account ")
    

# class ATM(User_manager):
#     print(hello)


def main():
    customer_list=[]
    Managers=User_manager()
    while True:
        print("1 = Creating New Account ")
        print("2 = View Balance ")
        print("3 = Deposit ")
        print("4 = Withdraw ")
        print("5 = Close Account ")
        print("6 = exit")
        select1=int(input("select your choice : "))

        if select1 == 1:#Creating New Account
            while True:
                try:
                    print(" Welecome to Bank Of Broda ")
                    user_name=input("Enter user name : ")
                    mobile_no=int(input("Enter mobile number in digit : "))
                    address=input("Enter user Address : ")
                    while True:
                        balance=int(input("Enter opening balance : "))
                        if balance >= 10000:
                            opening_balance=balance
                            break
                        else:
                            print("Please enter minimum amount is 10000 ")

                    user_ditails=Users(user_name,mobile_no,address,opening_balance)
                    Managers.users_list.append(user_ditails)
                except :
                   raise
                else:
                    break
        elif select1 == 2:#View Balance
            try:
                print(" Welecome to Bank Of Broda ")
                while True:
                    Account_no=int(input("Enter Account Number : "))
                    list_users=Managers.users_list
                    print()
                    for user in list_users:
                        print(user.account_no)
                        if Account_no == user.account_no:
                            print("Balance is : ",user.balance)
                            break
                        else:
                            print("Not Exit Your Account Number ")
                    break   
            except Exception as e:
                print(e)
        elif select1 == 3:#Deposit
            try:
                while True:
                    Account_no=int(input("Enter Account Number : "))
                    Balance=int(input("Enter Your Deposit Amount : "))
                    list_users=Managers.users_list
                    print()
                    for user in list_users:
                        if Account_no == user.account_no:
                            # print("Balance is : ",user.balance)
                            user.balance += Balance
                            print(user.balance)
                        else:
                            print("Not Exit Your Account Number ")
                    break 
            except Exception as e:
                print(e)
        elif select1 == 4:#Withdraw
            try:
               while True:
                    Account_no=int(input("Enter Account Number : "))
                    W_Balance=int(input("Enter Your Withdraw Amount : "))
                    list_users=Managers.users_list
                    print()
                    for user in list_users:
                        if Account_no == user.account_no:
                            # print("Balance is : ",user.balance)
                            user.balance -= W_Balance -0.5
                            print(user.balance)
                        else:
                            print("Not Exit Your Account Number ")
                    break 
            except Exception as e:
                print(e)
        elif select1 == 5:#Close Account
            print("hello5")
        elif select1 == 6:#exit
            break

main()