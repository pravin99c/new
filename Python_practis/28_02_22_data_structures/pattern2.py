# | = = = = = = = = = = = | 
# | \ 4 3 2 1 0 b c d e / | 
# | b \ 3 2 1 0 b c d / 1 | 
# | b c \ 2 1 0 b c / 2 1 | 
# | b c d \ 1 0 b / 3 2 1 | 
# | b c d e \ 0 / 4 3 2 1 | 
# | 0 0 0 0 0 X 0 0 0 0 0 | 
# | 1 2 3 4 / 0 \ e d c b | 
# | 1 2 3 / b 0 1 \ d c b | 
# | 1 2 / c b 0 1 2 \ c b | 
# | 1 / d c b 0 1 2 3 \ b | 
# | / e d c b 0 1 2 3 4 \ | 
# | = = = = = = = = = = = | 
n=5
num = ""
for i in range(-(n+1),n+2):
    for j in range(-(n+1),n+2):
        if abs(j)==n+1:
            num +="| "
        elif abs(i)==n+1:
            num += "= "
        elif i==0 and j==0:
            num += "X "
        elif i==0 or j==0:
            num += "0 "
        elif i-j==0:
            num += "\\ "
        elif abs(i)-abs(j)==0:
            num += "/ "
        elif abs(i)-abs(j)>=0 and (i>0 and j>0 or i<0 and j<0):
            num += str(abs(j))+" "
        elif abs(i)-abs(j)<=0 and (i>0 and j<0 or i<0 and j>0):
            num += str(n-abs(j)+1)+" "
        elif abs(i)-abs(j)<=0:
            num += chr(98+n-abs(j))+" "
        else:
            num += chr(97+abs(j))+" "
    num += "\n"

print(num)