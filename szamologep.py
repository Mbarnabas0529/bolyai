def adas(x,y):
        return x + y
def kivon(x,y):
        return x - y
def szoroz(x,y):
        return x * y
def oszt(x,y):
        return x / y
def negyzetreemel(x,y):
        return x ** y
muvelet = input("Adj meg egy számolást")
jelek = "+","-","*","/","**"
for i in range(len(muvelet)):
    print(muvelet[0],jelek,muvelet[1])