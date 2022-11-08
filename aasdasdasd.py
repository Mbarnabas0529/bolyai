dec1 = int(input("Irja be az 1. oktet értékét az íp címből (0-255):"))
dec2 = int(input("Irja be a 2. oktet értékét az íp címből (0-255):"))
dec3 = int(input("Irja be a 3. oktet értékét az íp címből (0-255):"))
dec4 = int(input("Irja be a 4. oktet értékét az íp címből (0-255):"))
if dec1 > 255:
    print("Ne adj meg nagyobb értéket az elsőnél😠")
if dec2 > 255:
    print("Ne adj meg nagyobb értéket a másodiknál 😠")
if dec3 > 255:
    print("Ne adj meg nagyobb értéket a harmadiknál😠")
if dec4 > 255:
    print("Ne adj meg nagyobb értéket a negyediknél 😠")
bin1 = ""
bin2 = ""
bin3 = ""
bin4 = ""
o1 = dec1   #????????????????????
o2 = dec2   #????????????????????
o3 = dec3   #????????????????????
o4 = dec4   #????????????????????
for i in range(7, -1, -1):
    if dec1 >= 0:
        bin1 = (str(dec1 % 2) + bin1)
        dec1 = dec1 // 2
for i in range(7, -1, -1):
    if dec2 >= 0:
        bin2 = (str(dec2 % 2) + bin2)
        dec2 = dec2 // 2
for i in range(7, -1, -1):
    if dec3 >= 0:
        bin3 = (str(dec3 % 2) + bin3)
        dec3 = dec3 // 2
for i in range(7, -1, -1):
    if dec4 >= 0:
        bin4 = (str(dec4 % 2) + bin4)
        dec4 = dec4 // 2
print(o1,o2,o3,o4,sep=".", end=" ")
print("ipv4 cím kettes számrendszerben kifejezve = ", end="")
print( bin1,bin2,bin3,bin4, sep=".")
fel2 = str(input("Írja be az ipv4-es címet (pl.:192.168.17.2):"))
print(fel2, "ipv4 cím kettes számrendszerben kifejezve =")
print(30*"-*")#orai asdasd

oktet = ""
for k in range(1,5):
    a = int(input("Irja be az 1. oktet értékét az ip címből (0-255): "))
    kettes = ""
    for i in range(7, -1, -1):
        if a - 2 ** i >= 0:
            x = 1
            a = a-2 ** i
        else:
            x = 0
        kettes = kettes + str(x)
    oktet = oktet + kettes+"."
print("Az",a,"ipv4 cím kettes számrendszerben = ",oktet)
ip = str(input("IPV4:"))

print(30*"-*")
