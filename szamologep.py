import math

feladat = input("Feladat: ")  # pl: 3!-25*3!+423**2-5!*3


def isFactorial(feladat):
    masolat = feladat

    for i in feladat:
        if not i.isdigit():
            if i != "!":
                masolat = masolat.replace(i, " ")

    for i in masolat.split():
        if "!" in i:
            feladat = feladat.replace(i, str(math.factorial(int(i[:-1]))))

    return eval(feladat)


print(isFactorial(feladat))
