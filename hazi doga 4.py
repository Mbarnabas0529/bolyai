mag =  float(input("Kérem adja meg a magasságát m-ben:"))
suly = float(input("Kérem adja meg a testtömegét kg-ban:"))
bmi = suly / (mag**2)

normmin = 18.5
normmax = 24.99

ideal1 =  normmin*(mag**2)
ideal1=round(ideal1,2)
ideal2 = normmax*(mag**2)
ideal2 =round(ideal2,2)

print("*"*30,"-"*5,"*"*30, sep="")
print("Az ön testtömegindexe:" , round(bmi,2),"%")
print("Az ön magasságához az ideális testtömeg:",ideal1,"kg","és",ideal2,"kg között van")


