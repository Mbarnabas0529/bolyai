A = int(input("Kérem az 1. számot:"))
B = int(input("Kérem a 2. számot:"))
J = str(input("Adja meg a műveleti jelet:[+,-,*,/,**,%]"))

if J == "+":
    print(A+B)
elif J == "-":
    print(A-B)
elif J == "*":
    print(A*B)
elif J == "/":
    print(A/B)
elif J == "**":
    print(A**B)
elif J == "%":
    print(A%B)

print(30*"-")
c = int(input("Szám:"))
kettes = ""
for i in range(7,-1,-1):
    if c - 2**i >= 0:
        x=1
        c = c-2**i
    else:
        x=0
    kettes = kettes + str(x)
print(kettes)
print(30*"-")
d = int(input("Adj meg egy pozitív egész számot:"))
prim=True
for i in range(2,d//2+1):
    if d%i==0:
        prim=False
        print("Az %i osztója %i-nek"%(i,d))
if prim:
     print("A %i primszam" %(d))

