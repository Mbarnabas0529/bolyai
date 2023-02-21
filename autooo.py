def atlag_fogyasztas(_fogyasztas):
    _szamlalo = 0
    _osszeg = 0
    for adat in _adat:
        _szamlalo += _osszeg + adat[_fogyasztas]
    return _osszeg/len(_adat)
adat = {}
_adat = {"auto","fogyasztas","evj"}

for i in range(len(_adat)):
    auto = input("adja meg az autó nevét:")
    if auto == "vege":
        break
    fogyasztas = int(input("adja meg az autó fogyasztását:"))
    evj = int(input("Adja meg az autó évjáratát:"))
    if evj > 2023:
        print("hamis évszám")
        evj = int(input("Adja meg az autó évjáratát:"))

    adat[auto] = {"fogyasztas":fogyasztas,"evjarat":evj}
    print(adat)

for _adat in adat.items():
    print("adat:",adat)


print('feladat b)')
for fogy in adat.values():
    print(fogy["fogyasztas"])
    print("Az autok atlag fogyasztasa:",atlag_fogyasztas("fogyasztas"))

print('feladat c')
