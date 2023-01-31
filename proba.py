osztaly = {}
def atlag (M,Ma,A,T,I):
    asd = M+Ma+A+T+I
    return float(asd/5)
name = ""
while name != " ":
    name = str(input("Adja meg a diák nevét: "))
    if name == " ":
        break
    _Magyar = int(input("Add meg a magyar jegy: "))
    _Matek = int(input("add meg a matek jegy: "))
    _Angol = int(input("Add meg az angol jegy: "))
    _Tori = int(input("Add meg a töri jegy: "))
    _Info = int(input("Add meg az info jegy: "))
    osztaly[name] = {}
    osztaly[name]["Magyar"] = _Magyar
    osztaly [name]["Matek"] = _Matek
    osztaly [name]["Angol"] = _Angol
    osztaly[name]["Töri"] = _Tori
    osztaly [name]["Info"] = _Info
    osztaly[name]["Átlag"] = atlag(_Magyar, _Matek, _Angol, _Tori, _Info)
    print(osztaly)