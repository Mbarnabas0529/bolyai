Sa = 2.7
Va = 50
Ta = Sa/Va
Sb = 7.9
Vb = 90
Tb = Sb/Vb
Sc = 29.7
Vc = 130
Tc = Sc/Vc
T1 = 28800-1320 #8:00-22p
H = T1//3600
H1 = T1%3600
M = H1//60
print("a.) feladat""\n",20*"-")
ans1 = Ta+Tb+Tc
print("a szükséges idő az egyetemig:", round(ans1, 2) ,"óra",)
print("b.) feladat""\n",20*"-")
print("a szükséges idő az egyetemig:", round(ans1*60),"perc",)
print("c.) feladat""\n",20*"-")
print(H,":",M,)




