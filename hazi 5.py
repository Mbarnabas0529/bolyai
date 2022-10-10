ev = int(input("Milyen év?"))
if 1984<=ev<=2043:
   szin_szam = ev % 10
if szin_szam == 4 or szin_szam==5:
    print("Zöld")
elif szin_szam == 6 or szin_szam==7:
    print("piros")
elif szin_szam == 8 or szin_szam==9:
    print("sarga")
elif szin_szam == 0 or szin_szam==1:
    print("feher")
elif szin_szam == 2 or szin_szam==3:
    print("fekete")
else:
    print("Nem megfelelő a megadott szám!")

