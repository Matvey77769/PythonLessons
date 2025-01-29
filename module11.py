file = open("perepis.txt","r")
k = 0

d1 = int(input("Укажите меньшее число диапазона"))
d2 = int(input("Укажите Большее число диапазона"))
for i in file:
    L = i.split()
    year = L[3][-2:]
    if int(year) < 78:
        k+=1
    if int(year)<=d2 and int(year)>=d1:
        print(i)
print("Рожденные до 78: ",k)
file.close()

