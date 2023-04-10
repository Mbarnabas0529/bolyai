print("Feladat 1)")
def ter():
    a = int(input("a:"))
    b = int(input("b:"))

    t = a*b

    return t


print(f"T:{ter()}")
print("\n")

print("Feladat 2)")
def lnko():
    sz1 = int(input("szám1:"))
    sz2 = int(input("szám2:"))
    while sz2:
        sz1,sz2 = sz2, sz1%sz2
        return sz1
print(lnko())
print("\n")

print("Feladat 3)")

def oszto_szam(szam):
    szamlalo = 0
    for i in range(1, szam+1):
        if szam % i == 0:
            szamlalo += 1
    return szamlalo

szam = int(input("Add meg a számot: "))
print("A(z)", szam, "számnak", oszto_szam(szam), "osztója van.")

def prim():
    n = int(input("adj meg egy számot:"))
    if n / n == 1 and n/1 == n:
        return "prím"
    else:
        return "Ez nem prím"
print(prim())
print("\n")

print("Feladat 5)")
print("\n")
def lista_hossza(lista):
    szamlalo = 0
    for elem in lista:
        szamlalo += 1
    return szamlalo

my_list = []

while True:
    uj_dolog = input("Írj be valamit a listához: ")
    if uj_dolog == "":
        break
    my_list.append(uj_dolog)

hossz = lista_hossza(my_list)
print(f"Az általad megadott listának {hossz} eleme van.")


print("Feladat 6)")
print("\n")

print("Feladat"" 7)")
print("\n")

print("Feladat 8)")
print("\n")
def atlag(lista):
    if len(lista) == 0:
        return None
    return sum(lista) / len(lista)

lista = []
while True:
    elem = input("Add meg egy elemet: ")
    if elem == "":
        break
    lista.append(int(elem))

if len(lista) > 0:
    print(f"A lista elemeinek átlaga: {atlag(lista)}")
else:
    print("A lista üres.")

print("Feladat 9)")
print("\n")
def harommal_oszthato_de_nem_ottel(szamok):
    darab = 0
    for szam in szamok:
        if szam % 3 == 0 and szam % 5 != 0:
            darab += 1
    return darab

szamok = []
while True:
    szam = input("Adj meg egy számot, vagy írj 'exit'-et a kilépéshez: ")
    if szam == 'exit':
        break
    szamok.append(int(szam))

print(f"A listában {harommal_oszthato_de_nem_ottel(szamok)} db 3-mal osztható, de 5-tel nem osztható szám van.")

