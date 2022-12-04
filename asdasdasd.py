list=[-14,23,1,-48,-43,28,-77,-33,-95,38,-9,98,-61,58,21,87,41,-65,-22,-20,-56,-75,80,-77,100,67,22,8,-78,-6]

walter = 0
for e in list:
    if e:
        walter += 1
print(walter,"eleme van")

neg = len(list)
minusz = -20
i = 0
while list[i] != minusz:
    i += 1
print("Van minusz érték")

parosindex = []
p = 0
for i in list:
    if i % 2:
        parosindex.append(i)
        p += 1
print(p,"db van")

maximum = list[0]
for m in range(1,len(list)):
    if list[i] > m:
        maximum = list[i]
print(maximum)

oszthato10 = []
for t in range(len(list)):
    if list[t] % 10 == 0:
        oszthato10.append(list[t])
print("osztható 10-zel:",oszthato10)

igham = []
for ih in list:
    if ih % 2:
        igham.append(i)
print("Hamis")

adas = 0
atlag = len(list)
for at in list:
    adas = adas + at
    adas = adas / atlag
print(adas)

oszto = []
for o in range(len(list)):
    if list[o] % 17 == 0:
        oszto.append(list[o])
print(oszto,"nincs ilyen szám")