dec1 = int(input("Irj be a 1. oktet értékét az íp címből (0-255):"))
dec2 = int(input("Irj be a 1. oktet értékét az íp címből (0-255):"))
dec3 = int(input("Irj be a 1. oktet értékét az íp címből (0-255):"))
dec4 = int(input("Irj be a 1. oktet értékét az íp címből (0-255):"))
bin1 = ""
bin2 = ""
bin3 = ""
bin4 = ""
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
print(dec1,dec2,dec3,dec4,"ipv4 cím kettes számrendszerben kifejezve =",bin1,bin2,bin3,bin4, sep=".")