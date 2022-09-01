string = input("Enter the string : ")
list_words = string.split()

set_words = set(list_words)

#number of unique words
print("number of unique words :", len(set_words))

#printing unique words
print(set_words)
