k = int(input("Hány csupor méz van otthon?"))
x = int(input("Hány kilómétert tesz meg Malackához?"))
y = int(input("Hány km-nél megy be Nyuszihoz?"))
n = int(input("Hány csupor mézet kapott Nyuszitól?"))

if k>x:
    print(k-x+n,"maradt Malackának")
else:
    print("0 csupor méz maradt Malackának")


