print("1. feladat)")
def masodik(szoveg):
    szoveg2 = ""
    for i in range(len(szoveg)):
        if i% 2 == 1:
            szoveg2 += szoveg[i].upper()
        else:
            szoveg2 += szoveg[i]

    return szoveg2
szoveg = input("Adj meg egy szöveget:")
print("Az átalakított szöveg:", masodik(szoveg))
print("2. feladat)")

def kodol(szoveg):
    szoveg3  = ""
    for kar in szoveg:
        if kar.isalpha():
            kovetkezo_kar=chr((ord(kar)-65+1)%26+65)
            szoveg3 += kovetkezo_kar
        else:
            szoveg3 += kar
    return szoveg3
szoveg = input("adj meg egy szövegeeet:")
print("A visszaléptetett szöveg:",kodol(szoveg))#ABCDEFGHIJKLMNOPQRSTUVWXYZ
print("3. feladat)")
def vignere(index):
    sor=""
    for i in range(26):
        karakter = chr((i+index) % 26 + 65)
        sor += karakter
    return sor
def vignere_tabla():
    tabla=""
    for i in range(10):
        tabla += vignere(i) + "\n"
    return tabla
tabla = vignere_tabla()
print("Vignere tabla:\n",tabla)