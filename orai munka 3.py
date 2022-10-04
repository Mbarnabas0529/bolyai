a = int(input("Adj meg egy egész értéket:"))
if a%2==0:
    print("páros")
else:
    print("páratlan")
#feladat1

szo = input("Adjon meg egy szót:")
if szo=="tűzliliom":
    print("Ezt ismerem, ez egy csodaszép virág!")
else:
    print("Ez nagyon szép szó")
#feladat2

jövedelem = int(input("Add meg a jövedelmedet:"))
if jövedelem<=14399:
    print("nem kell adót fizetned")
elif 33999>=jövedelem>=14400:
    print("19% adót kell fizetned ami",jövedelem*0.19,"euro" )
elif jövedelem>=34000:
    print("29% adót kell fizetned ami",jövedelem*0.29,"euró")
#feladat3

mag =  float(input("Kérem adja meg a magasságát m-ben:"))
suly = float(input("Kérem adja meg a testtömegét kg-ban:"))
bmi = suly / (mag**2)

print("Az ön testtömegindexe:" , round(bmi,2),"%")
if bmi<16:
    print("súlyos soványság")
elif bmi<=16.99:
    print("mérsékelt soványság")



