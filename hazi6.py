szam=int(input("Adj meg egy számot: "))
szam2=0
while szam!=1:
    if szam%2==0:
        szam2+=1
        szam=szam / 2
    elif szam%2 == 1:
        szam2+=1
        szam=szam + 1
    print("A", szam2, "elem: ", int(szam))
