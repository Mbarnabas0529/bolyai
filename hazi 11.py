lista=[-14, 23, 1, -48, -43, 28, -77, -33, -95, 38, -9, 98, 61, 58, 21, 87, 41, -65, -22, -20, -56, -75, 80, -77, 100, 67, 22, 8, -78, -6]
lista.sort()
print("1. feladat")
plusz = 23
i = 0
while lista[i] != plusz:
    i += 1
print("Van plusz érték")
print("\n")
print(30*"-*")

print("2. feladat")
elem = 0
for e in lista:
    if e:
        elem += 1
print(elem,"eleme van")
print("\n")
print(30*"-*")

print("3. feladat")

lista.sort()
print(lista[0],"a legkisebb érték")
print("\n")
print(30*"-*")

print("4. feladat")
oszto = []
for i in range(len(lista)):
    if lista[i] % 33 == 0:
        oszto.append(lista[i])
index = lista.index(-33)
print(oszto,"helye:",index)
print("\n")
print(30*"-*")

print("5. feladat")
ad = 0
for x in lista:
    ad = ad + x
atlag = ad / len(lista)
print(atlag/2)
print("\n")
print(30*"-*")

print("6. feladat")
igazhamis = []
for i in lista:
	if i / 2 == -3.5:
		igazhamis.append(i)
print("hamis")
print("\n")
print(30*"-*")

print("7. feladat")
neg_szam = 0
for szam in lista:
    if szam >= 0:
        neg_szam += 1
print(neg_szam)
print("\n")
print(30*"-*")

print("8. feladat") # nem jól működik
if index+1 == -95:
    print("van")
print("\n")
print(30*"-*")

print("9. feladat")
oszto = []
for i in range(len(lista)):
    if lista[i] % 19 == 0:
        oszto.append(lista[i])
print(oszto[1],"helye:",lista.index(oszto[1]))
print("\n")
print(30*"-*")

print("10. feladat")
oszto = []
for i in range(len(lista)):
	if lista[i] % 5 == 0:
		oszto.append(lista[i])
print(oszto)
