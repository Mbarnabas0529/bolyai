animals = {}
nev2 = ""
sorszam = 0
while True:
    nev = input("nev: ")
    if nev == "":
        break
    fajta = input("Fajta: ")
    kor = int(input("Kor: "))
    szul_ev = 2023 - kor
    animals[nev] = {"fajta": fajta, "szul_ev": szul_ev}
for nev, info in animals.items():
    sorszam += 1
    print(f"{sorszam}.",'allat')
    print(f"- Nev --> {nev}","\n"
          f"- fajta --> {info['fajta']}","\n"
          f"- ev --> {info['szul_ev']}")