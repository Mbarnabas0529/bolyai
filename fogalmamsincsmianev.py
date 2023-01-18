dictionary = {
              "cat": "cica",
              "dog": "kutya",
              "horse": "ló",
              "parrot": "papagáj",
              "bear": "medve",
              }
words=""
#dictionary['swan'] = 'hattyú'
while dictionary != words:
    if words == " ":
        break

    words = input("Words: ")

    if words in dictionary:
        print(words,"=",dictionary[words])
    else:
        print(words,"=","is not in dictionary")
print(30*"-*")
dictionary3 = {
              "cat": "cica",
              "dog": "kutya",
              "horse": "ló"
              }
for i in range(10):
    new_word = input("Uj szo: ")
    new_key = input("Uj jelentes: ")
    dictionary3.update({new_word:new_key})
print(dictionary3)
print(30*'-*')
for english, magyar in dictionary.items():
    print(english, "->", magyar)
print(30 * "-*")
x = dictionary.get(input("Minek a jelentését akarod tudni:"))

print(x)




