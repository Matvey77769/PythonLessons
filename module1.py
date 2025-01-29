file = open("perepis.txt","r")
k = 0
for i in file:
    L = i.split()
    if int(L[3][-2:]) < 78:
        k+=1
print(k)
file.close()

