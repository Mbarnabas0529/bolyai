dictionary = {
              "cat": "cica",
              "dog": "kutya",
              "horse": "ló"
              }
words=""
while dictionary != words:
    if words == " ":
        break
    words = input("Words: ")

    if words in dictionary:
        print(words,"=",dictionary[words])
    else:
        print(words,"=","is not in dictionary")
print('\n')
#f2
dictionary = {
              "cat": "cica",
              "dog": "kutya",
              "horse": "ló"
              }
for key in dictionary.keys():
    print(key, "->", dictionary[key])

