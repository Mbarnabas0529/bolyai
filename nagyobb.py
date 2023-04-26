x = int(input("adj meg egy számot:"))
y = int(input("adj meg egy számot:"))

if x > y:
    print("A nagyobb érték:",x)
elif y > x:
    print("A nagyobb érték:",y)
elif y == x:
    print("A két érték egyenlő")