t=int(input())
for i in range(t):
    n=int(input())
    sl=[]
    ans=0
    for j in range(n):
        l=input()
        sl.append(set(l))
    last_list=set(sl[0])
    print(last_list)
    for j in range(1,len(sl)):
        last_list=last_list.intersection(sl[j])
    print(last_list)
        