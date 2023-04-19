print('Feladat 1)')
x = int(input("Adj meg 1 számot:"))
y = int(input("Adj meg 1 számot:"))

if x < y:
    print(y)
else:
    print(x)
print('Feladat 2)')

def kodolas():
    muv = ""
    szoveg = input("Adj meg egy szöveget:")
    betu = input("Adj meg egy kicserélendő betűt:")

    for ltr in szoveg:
        if ltr == betu:
            muv += str(ord(ltr))
        else:
            muv += ltr

    return muv
print(kodolas())

print("feladat 3)")
with open("autok.csv","r", encoding="utf-8") as f:
    fejlec = f.readline().strip().split(";")
    dbszam = len(fejlec)