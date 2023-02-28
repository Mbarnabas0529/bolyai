autok = []
egy_auto={}
nev = "1"

def szam_e(_szam,szamjegy=None):
    jo = True
    for egy_szam in _szam:
        if not (egy_szam.isnumeric() or egy_szam == "."):
            jo = False
            break
    if not jo:
        print("A megadott adat nem megfelelő")
    return jo
def oreg(_autok):
    min = autok[0]['ev']
    min_nev = autok[0]["nev"]
    for _auto in autok:
        if min >_auto["ev"]:
            min=_auto["ev"]
            min_nev = _auto["nev"]
    return min_nev
def atlag_fogy(_autok):
    osszeg=0
    for i in range(len(_autok)):
        osszeg+=float(autok[0]["fogy"])
    return round(osszeg/len(_autok),2)
def nevek(_autok): return _autok["nev"]
def rendezes2(_autok,sort_on="nev"):
    decorated = [(dict_[sort_on],dict_)for dict_ in _autok]
    decorated.sort()
    for (key,_dict) in decorated:
        vissza.append()

    decorated.sort()
    return [dict_ for (key,dict_) in decorated]
def rendezes(_autok,sort_on="nev"):
    decorated=[]
    vissza = []
    for dict_ in _autok:
        decorated.append((dict_[sort_on],dict_))
    decorated.sort()
    for (key,_dict) in decorated:
        vissza.append(_dict)
    return vissza
snev = "a"
while snev!=":"
    snev = input("Kérem adjon meg egy nevet:")
    if

        auto["fogy"]=input("Kérem adja meg az auto fogyasztását")
        while not szam_e(auto["fogy"]):
            auto["fogy"]=input("Kérem adja meg az auto fogyasztását")
        auto["nev"]=snev
        autok.append(auto)
    auto={}
print(autok)
#legoregebb
print("legregebbi auto:",oreg(autok))
#atlagfogyasztas
print("az autok atlagos fogyasztasa:",atlag_fogy(autok))
#abc
print(sorted)
