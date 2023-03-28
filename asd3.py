with open("programnyelv_1feladat.txt", "r", encoding="utf-8") as f:
    f.readline()
    f.readline()
    with open("programnyelv_masolat.txt", "w", encoding="utf-8") as cel:
        for sor in f:
            nyelv_l=sor.strip().split(";")
            #print(nyelv_l[0]+";"+nyelv_l[1],file=cel)
            cel.writelines(nyelv_l[0]+";"+nyelv_l[1]+"\n")
print("Melyik ismétlődik?")
