print('Feladat 1)')
x = int(input("Adj meg 1 számot:"))
y = int(input("Adj meg 1 számot:"))

if x < y:
    print(y)
else:
    print(x)
print('Feladat 2)')

def kodolas(_szoveg,_betu):
    muv = ""
    for ltr in szoveg:
        if ltr == betu:
            muv += str(ord(ltr))
        else:
            muv += ltr
    return muv
szoveg = input("Adj meg egy szöveget:")
betu = input("Adj meg egy kicserélendő betűt:")

print(kodolas(szoveg,betu))

print("feladat 3)")
autok = []#osszes auto
egy_auto = []
ferohely = 0
_ferohely = 0
atlag = 0
with open("autok.csv","r", encoding="utf-8") as f:
    f.readline()
    for sor in f:
        egy_auto = sor.strip().split(";")
        autok.append(egy_auto)
print(autok)
print('3B)')
for egy_auto in autok:
    if egy_auto[0]=="Munkács" and egy_auto[1]=="Záhony":
        ferohely+=int(egy_auto[4])
print(ferohely)

print('3C)')
for egy_auto in autok:
    if egy_auto[4]:
        _ferohely += int(egy_auto[4])
        atlag = _ferohely/len(autok)
print(round(atlag,1))
print('3D')
with open("budapestrol.dat","w",encoding="utf-8") as b:
    for egy_auto in autok:
        if egy_auto[0] == "Budapest":
            print(";".join(egy_auto),file=b)