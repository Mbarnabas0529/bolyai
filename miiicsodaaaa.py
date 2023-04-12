print("Feladat 1)")
a = int(input("Adj meg egy számot:"))

if a % 2 == 0:
    print("Páros")
else:
    print("páratlan")
print("\n")

print("Feladat 2)")

def email():
    nev = input("Adj meg nevet:")
    osztaly = (input("Add meg az osztályod betujet:"))
    ev = input("Add meg a kezdési éved:")

    return f"{nev}.tech{ev}{osztaly}@bolyaimovar.com"
print(email())