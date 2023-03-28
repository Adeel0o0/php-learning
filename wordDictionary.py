

def main():
    word_dictionary = {
        "Hi": "a way of greeting",
        "Eyes": "An organ used for seeing",
        "Earth": "A planet in space",
    }
   
    while True:
     word = input("Enter a word: ")
     if word == "":
         break
     if word in word_dictionary:
         print(word, ":", word_dictionary[word])


main()