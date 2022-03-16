list1= [11, 45, 8, 23, 14, 12, 78, 45, 89]

d=[]
for i in range(0,len(list1),3):
    a=list1[i:i+3][::-1]
    d.append(a)
print(d)