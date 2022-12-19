#megoldas 1
fakt = 1
def osszead(x, y):
    return x + y
def kivon(x, y):
    return x - y
def szoroz(x, y):
    return x * y
def oszt(x, y):
    return x / y
def negyzet(x, y):
    return x ** y
print("1: osszead")
print("2: kivon")
print("3: szoroz ")
print("4: oszt")
print("5. negyzetreemel")
print("6. faktorialis")

valaszt = input("(1/2/3/4/5/6):")
if valaszt in ('1', '2', '3', '4','5',):
        szam = float(input("Elso ertek:"))
        szam2 = float(input("Masodik ertek:"))

if valaszt == '1':
     print(szam, "+", szam2, "=", osszead(szam, szam2))

elif valaszt == '2':
    print(szam, "-", szam2, "=", kivon(szam, szam2))

elif valaszt == '3':
    print(szam, "*", szam2, "=", szoroz(szam, szam2))

elif valaszt == '4':
    print(szam, "/", szam2, "=", oszt(szam, szam2))

elif valaszt == '5':
    print(szam,"^", szam2, "=", negyzet(szam,szam2))

elif valaszt == '6':
    szam3 = int(input("Ird be a szamot:"))
    for i in range(1, szam3 + 1):
            fakt = fakt * i
    print("Faktoriálisa", szam3,"-nak/-nek" "=", fakt)
#megoldas 2??
print("az eredény:",eval(input("Adj meg egy számolást:")))
