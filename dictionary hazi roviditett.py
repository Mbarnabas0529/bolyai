def atlag_szamitas(jegyek):
    osszeg = 0
    szamlalo = 0
    for jegy in jegyek.values():
        osszeg += jegy
        szamlalo += 1
    return osszeg / szamlalo

osztaly = {}
while True:
    _nev = input("Kérem adja meg a tanuló nevét:")
    if _nev == "":
        break
    _jegyek = {"magyar":0,"matek":0,"töri":0,"angol":0,"info":0}
    for targy in _jegyek.keys():
        _jegyek[targy] = int(input(targy + ":"))
    osztaly[_nev] = _jegyek

targy_osszeg = {"magyar":0,"matek":0,"töri":0,"angol":0,"info":0}
targy_szamlalo = {"magyar":0,"matek":0,"töri":0,"angol":0,"info":0}
for tanulo_neve, tanulo_jegyei in osztaly.items():
    print(f"{tanulo_neve} átlaga: {atlag_szamitas(tanulo_jegyei)}")
    for targy in tanulo_jegyei.keys():
        targy_osszeg[targy] += tanulo_jegyei[targy]
        targy_szamlalo[targy] += 1

for targy in targy_osszeg.keys():
    print(f"{targy} átlaga: {targy_osszeg[targy] / targy_szamlalo[targy]}")