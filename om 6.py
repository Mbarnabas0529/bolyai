n = int(input("Adjon meg egy számot: "))
m = int(input("Adjon meg még egy számot: "))
for i in range(n, m): # i felveszi a range altali elemeket m-ig vegig lepked
    if i % 2 == 0:
        print(i,end="-", )


#feladat2
print("\n",30*"-")
szam = 0
osszeg = 0
sor = 1
while szam<10:
    szam = int(input("10-nél kisebb szam:"))
    osszeg=szam+osszeg
    sor+=1
    if szam > 10:
        print("az utolsó szám nem kisebb 10-nél")
        print("a tíznél kisebb számok összege:",osszeg-szam)
#feladat3
print("\n",30*"-")
a = float(input("Adja meg a háromszög A oldalának hosszát:"))
b = float(input("Adja meg a háromszög B oldalának hosszát:"))
c = float(input("Adja meg a háromszög C oldalának hosszát:"))

if (a+b>c) and (b+c>a) and (a+c>b):
    T=(a+b+c)/2
    K=a+b+c
    print("A háromszög megszerkeszthető""\n","A háromszög kerülete:",K,"A háromszög területe:",T,)
else:
    print("Nem lehet megszerkeszteni")




