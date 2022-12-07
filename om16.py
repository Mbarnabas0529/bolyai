szo = str(input("Adj meg egy szöveget:"))
for i in range(len(szo)):
    print(chr(ord(szo[i])-32),end="")
print("\n")
print(30*"-*")
szo1 = str(input("Adj meg egy szöveget:"))
for i in range(len(szo1)-1,-1,-1):
    print(chr(ord(szo[i])-32),end="")
print("\n")
print(30*"-*")
mondat = str(input("Adj meg egy mondatot:"))
for i in range(len(mondat)):
    print(chr(ord(mondat[i])-32),end="")
print("\n")
print(30*"-*")

