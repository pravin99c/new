l1=[2, 2]
l2=[6,6]
r1=[4,4]
r2=[8,8]

L1=[]
R1=[]
L2=[]
R2=[]

L1.append(min(l1[0],l2[0]))
L1.append(min(l1[1],l2[1]))

L2.append(max(l1[0],l2[0]))
L2.append(max(l1[1],l2[1]))

R1.append(min(r1[0],r2[0]))
R1.append(min(r1[1],r2[1]))

R2.append(max(r1[0],r2[0]))
R2.append(max(r1[1],r2[1]))

def overlappingArea(L1, R1, L2, R2):
    x = 0
    y = 1
 
    x_dist = (min(L2[x], R2[x]) - max(L1[x], R1[x]))
    y_dist = (min(L2[y], R2[y]) - max(L1[y], R1[y]))
    areaI = 0
    if x_dist > 0 and y_dist > 0:
        areaI = x_dist * y_dist
    return areaI
print(overlappingArea(L1, R1, L2, R2))