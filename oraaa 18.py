def demo():
    global str
    print(str)
    str = "you are smart"
    print(str)
#global scope
str = "you are clever"
demo()
print("\n")
#EZ A HIBAS :sob:

#def demo():
 #   print(str)
  #  str = "you are smart"
   # print(str)
#global scope
#str = "you are clever"
#demo()
#print(str)

def minimum(_lista):
   _lista.sort()
   return _lista[0]

szam = 1
lista=[]
while szam!=0:
    szam = int(input("Adj meg egy számot:"))
    if szam != 0:
        lista.append(szam)
print("Legkisebb szám:",minimum(lista))