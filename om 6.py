n = int(input("Adjon meg egy számot: "))
m = int(input("Adjon meg még egy számot: "))
for i in range(n, m): # i felveszi a range altali elemeket m-ig vegig lepked
    if i % 2 == 0:
        print(i,end="-", )


#feladat2
print("\n",30*"-")
szam = 0
sor = 1
sor += 1

while szam<10:
    szam = int(input("10-nél kisebb szam"))
#feladat3
