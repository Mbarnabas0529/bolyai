orszagok=[]
csati=[]
def talalo(_talalok):
    return _talalok['csatlakozas']
with open("eu.csv","r+",encoding="utf-8") as forras:
    for sor in forras:
        orszagok_lista=sor.strip().split(",")
        egy_orszag={"orszag":orszagok_lista[0],"főváros":orszagok_lista[1],"csatlakozas":orszagok_lista[2]}
        orszagok.append(egy_orszag)
print(orszagok)
for orszag in orszagok:
    print(orszag['orszag'])
#for fovaros in orszagok:
    #print(fovaros['főváros'])
orszagok.sort(key=talalo)
print(orszagok)
