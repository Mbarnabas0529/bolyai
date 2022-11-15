lista = [32,5,12,8,3,75,2,15]
lista.sort()
lista.reverse()
print("a lista legnagyobb elemének az értéke:",lista[0])
print(30*"-*")
x = [32,5,12,8,3,75,2,15]
max = x[0]
index=0
for i in x:
    if max<i:
        max=i
print(max)
print(30*"-*")
lista2 = [32,5,12,8,3,75,2,15]
n = lista2[0]
for i in range(len(lista2)):
    if n<x[i]:
        n=lista2[i]
        n_i=i
print(n,n_i)
print(30*"-*")
