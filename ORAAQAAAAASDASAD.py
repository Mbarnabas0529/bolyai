szamok = [17,38,10,25,72]
szamok.sort()
print(szamok)
szamok.reverse()
print(szamok)
print(sorted(szamok))
lista1=[-14,23,1,-48,-43,28,-77,-33,-95,38,-9,98,-61,58,21,87,41,-65,-22,-20,-56,-75,80,-77,100,67,22,8,-78,-6]

akarmilyen = "ez egy string"
for i in range(len(akarmilyen)):
    print(akarmilyen[i], end="")
print("\n")
print("-*"*30)
a = str(input("Adj meg egy szöveget:"))
for i in range(len(a)):
    print(a[i],end=" ")
print("\n")
print("-*"*30)
b = str(input("Adj meg egy szöveget:"))
for r in range(len(b)):
    if r%2 != 0:
        print(b[r],end=" ")
print("\n")
print("-*"*30)
c = str(input("Adj meg egy szöveget:"))
char = "" # space
for i in range(len(c)):
    print(ord(c[i]),end=" ")
print("\n")
print("-*"*30)
d = str(input("Adj meg egy szöveget:"))

