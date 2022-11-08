listam=['hétfő ', 'kedd', 'szerda', 1800, 20.357, 'csütörtök', 'péntek']

print(listam)
for i in range(7):
    print(listam[i])
print(30*"*-")
for i in listam:
    print(i)
print(30*"-*")
listam.append('szombat')
print(listam)
print(30*"-*")
listam.insert(1, "narancs")
print(listam)
print(30*"*-")
list = ['hétfő ', 'kedd', 'szerda', 1800, 20.357, 'csütörtök', 'péntek']
del(list[4])
print(list)
print(30*"-*")
del(list[3:4])
print(list)
print(30*"-*")
x=[20,22,44,55,32,86,95,34,26,77]
x.sort()
print(x)
print(30*"-*")
y =[20,22,44,55,32,86,95,34,26,77]
y.reverse()
print(y)
ind = [20,22,44,55,32,86,95,34,26,77]
print(ind.index(44))