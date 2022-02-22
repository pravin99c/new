# from tkinter.tix import FileSelectBox


num=5
s=0
for i in range(1,num+1):
    s+=pow(10,i-1)
    print(s*i)

#fib

def fib(n):
    a,b=0,1
    while(a<n):
        print(a,end=',')
        a,b=b,a+b
fib(10)