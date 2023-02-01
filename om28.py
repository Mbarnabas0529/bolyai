osztaly = {}
def atlag(M,MA,A,T,I):
    asd = M+MA+A+T+I
    return float(asd/5)


nev = input("Adja meg a nevet:")
while nev != 'Finish':
    _Magyar = input("Adja meg a Magyar jegyét:")
    _Matek = input("Adja meg a Matek jegyét:")
    _Angol = input("Adja meg a Angol jegyét:")
    _Tori = input("Adja meg a Töri jegyét:")
    _Info = input("Adja meg a Infó jegyét:")
osztaly[nev] = {}
osztaly[nev]["Magyar"] = _Magyar
osztaly[nev]["Matek"] = _Matek
osztaly[nev]["Angol"] = _Angol
osztaly[nev]["Tori"] = _Tori
osztaly[nev]["Info"] = _Info
osztaly[nev]["Atlag"] = atlag(_Magyar,_Matek,_Angol,_Tori,_Info)




