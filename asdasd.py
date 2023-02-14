def ember_atlag(_nev):
    _osszeg = 0
    for _targy in jegyek:
        _osszeg = _osszeg + int(osztaly[_nev][_targy])
    return _osszeg/len(jegyek)

osztaly = {}
jegyek = ["magyar","matek","angol","töri","info","fizika"]
osszeg = 0
vege = True
while True:
    _nev = input("Kérem adja meg a tanuló nevét:")
    _jegyek = {}
    if _nev == "":
        break
    for targy in jegyek:
        jegy = '0'
        while True:
            jegy = input(targy + ":")
            if jegy in "12345" and jegy !="":
                break
            print("hibas az adat, 1-5 Között adjon meg számokat!")


        _jegyek[targy] = jegy
    osztaly[_nev] = _jegyek
    print(osztaly)


for nev, tantargy in osztaly.items():
    print(nev,"atlaga:",ember_atlag(nev))

osszeg = 0
for nev in osztaly.keys():
    osszeg +=  ember_atlag(nev)
print("osztály átlag:","--->",osszeg/len(osztaly))

osszeg = 0
for targy in jegyek:
    for nev in osztaly.keys():
        osszeg += int(osztaly[nev][targy])
    print(targy,"atlag:",osszeg/len(osztaly))
