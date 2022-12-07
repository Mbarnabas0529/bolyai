def paros_e(szam):
    szoveg="a szam nem paros"
    if szam % 2 == 0:
        szoveg = "paros"
    return szoveg
def osszeg_fg(_egy_,_ketto_):
be = 1
lista=[]
osszeg = 0
while be != 0:
    be = int(input("Adj meg egy értéket:"))
    print(paros_e(be))
    osszeg = osszeg_fg(osszeg,be)
    #osszeg+=be
    print(paros_e(be))

print("a szamok osszege:",osszeg)