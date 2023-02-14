ember = {'név':'Géza',
         'születési_év':1999,
         'lakhely':'Makkoshotyka',
         'foglalkozás':'szarvasmarha-tenyésztő',
         'szemei száma':2,
         'kedvenc lottószámok':[1,2,3,4,5]
         }
words = ""
ember['kutya'] = 'Bodri'
ember['születési_év'] = 1980
del ember['szemei száma']
print("Keys:", ember.keys())

print(30*"-*")

print("kigyujtott ertekek:", ember.values())
print(30*"-*")
for key in ember.keys():
    print(key, ":", ember[key])
print(30*"-*")
print("ember neve:", ember.get('név'))

print(30*"-*")
print("2. feladat")
asd = {

   }
new_word = " "
while asd != new_word:
    if new_word == "":
        break
    new_word = input("szerzo: ")
    new_key = input("cim: ")
    asd.update({new_word: new_key})

print(asd)


