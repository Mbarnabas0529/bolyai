dec = int(input("adj meg egy számot:"))
bin = 0
a = 0
b = dec

while b > 0:
    bin = ((b%2)*(10**a)) + bin
    b = int(b/2)
    a += 1

print("A szám bináris alakja:",bin)