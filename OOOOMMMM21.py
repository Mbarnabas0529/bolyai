#ha nem irok pontot mukodik
ev = (input("Add meg a születési évedet ÉÉÉÉ.HH.NN-formátumban:"))
x = 0
for e in ev:
    if e != '.':
        e = int(e)
        x = x + e
if len(ev) != 8:
    print("HOSSZU A SZAM, NE HAZUDJ!444!!!!!")
else:
    while len(ev) > 1:
        asd = 0
        for i in ev:
            asd += int(i)
            print(ev)
            ev = str(asd)
print("Digit of Life:", ev)



#arian feladat:
def digit(be):
    x = 0
    for i in be:
        if i != ".":
            i = int(i)
            x = x + i
    return str(x)
a = input("ÉÉÉÉ.HH.NN.: ")

eredmeny = digit(a)

while len(str(eredmeny)) != 1:
    eredmeny = digit(eredmeny)

print("Keresett szam: ",eredmeny)

print("2. feladat")

