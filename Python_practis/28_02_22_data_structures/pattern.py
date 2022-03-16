n = int(input("Enter your number : "))
num=""
for i in range(-(n+1),n+2):
    for j in range(-(n+1),n+2):
        if abs(i)==n+1 or abs(j)==n+1 or i==0 and j==0:
            num += "0 "
        elif abs(i)-abs(j)>=0 and (i>0 and j>0 or i<0 and j<0):
            num += str(abs(i)-abs(j)+1)+" "
        elif abs(i)-abs(j)<=0 and (i<0 and j>0 or i>0 and j<0):
            num += str(n-(abs(j)-1))+" "
        else:
            num += "  "
    num += "\n"
print(num)