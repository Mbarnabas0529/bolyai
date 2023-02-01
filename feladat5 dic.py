orszagok = {}
fovaros = ""
sorszam = 0
while fovaros != " ":
    fovaros = input("Neve: ")
    if fovaros == "":
        break
    faj = input("Fovaros: ")
    kor = int(input("EU Csatlakozasi eve: "))

    orszagok[fovaros] = {"fajta": faj, }

for fovaros, info in orszagok.items():
    sorszam += 1
    print(f"{sorszam}. Orszag")
    print(f" - Orszag --> {fovaros}")
    print(f" - Fovaros --> {info['fajta']}")
    print(f" - EU Csatlakozasi eve --> {kor}")
