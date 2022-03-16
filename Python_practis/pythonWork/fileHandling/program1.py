file=open('file.txt','w')
file.write("Hello ")
file.write("sir")
file.close()
file=open('file.txt','r')
print(file.read())
file.close()
file = open('file.txt','a')
file.write("This will add this line")
file.close()

with open("file.txt", "w") as f:
    f.write("Hello World!!!")

