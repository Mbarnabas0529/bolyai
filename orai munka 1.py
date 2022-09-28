Va = int(input("Sebesség a lakott területen belül:"))
Vb = int(input("Sebesség a lakott területen kívül:"))
Vc = int(input("Sebesség az autópályán:"))
erkezes=int(input("Mikor érkezzen?:"))
Sa = 2.7
Sb = 7.9
Sc = 29.7

Ta = Sa/Va
Tb = Sb/Vb
Tc = Sc/Vc
ans1 = Ta+Tb+Tc


T1 = erkezes*60-ans1*60 #8:00-22p
H = T1//60
H1 = T1%60
M = round(H1)
print("a.) feladat:""\n",20*"-")
print("A szükséges idő az egyetemig:", round(ans1, 2) ,"óra","\n")
print("b.) feladat:""\n",20*"-")
print("A szükséges idő az egyetemig:", round(ans1*60),"perc","\n")
print("c.) feladat:""\n",20*"-")
print("Az indulási idő:",round(H),":",M, sep=" ")

