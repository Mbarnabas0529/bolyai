with open('parduc_2.feladat.txt','r',encoding='utf-8') as f:
    szoveg = f.read()
#betuszamolas
n_chrs = len(szoveg)
#maganhangzok
mgh = "aeiouáéíóöőúüű"
n_mgh = 0
for chr in szoveg:
    if chr in  mgh:
        n_mgh += 1
#szavak
szavak = szoveg.split()
n_szavak = len(szavak)

print(f"A vers {n_chrs} betűt tartalmaz")
print(f"A versben {n_mgh} magánhangzó található")
print(f"A versben összesen {n_szavak} szó fordul elő")
