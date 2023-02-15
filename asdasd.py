def ember_atlag(_nev):
    _osszeg = 0
    for _targy in jegyek:
        _osszeg = _osszeg + int(osztaly[_nev][_targy])
    return _osszeg/len(jegyek)
def ellenor(_jegy,_lista):
    vissza = True
    if _jegy not in _lista:
        vissza = False
        print("hibas az adat, 1-5 Között adjon meg számokat!")

    return vissza
def bekeres(__jegyek):
    vege = True

osztaly = {}
jegyek = ["magyar","matek","angol","töri","info","fizika"]



osztaly = bekeres(jegyek)
print(osztaly)
while True:
    _nev = input("Kérem adja meg a tanuló nevét:")
    _jegyek = {}
    if _nev == "":
        break
    for targy in jegyek:
        jegy = '0'
        while True:
            jegy = input(targy + ":")
            if ellenor(jegy,["1","2","3","4","5"]):
                break

        _jegyek[targy] = jegy
    osztaly[_nev] = _jegyek
    print(osztaly)


for nev, tantargy in osztaly.items():
    print(nev,"atlaga:",ember_atlag(nev))

osszeg = 0
for nev in osztaly.keys():
    osszeg +=  ember_atlag(nev)
print("osztály átlag:","--->",osszeg/len(osztaly))

for targy in jegyek:
    osszeg = 0
    for nev in osztaly.keys():
        osszeg += int(osztaly[nev][targy])
    print(targy,"atlag:",osszeg/len(osztaly))
