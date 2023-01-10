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
