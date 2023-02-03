#1. Count Letters

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
  counter = 0 
  for letter in letters:
    if letter in word:
      counter += 1
  return counter

print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

#2. Count X

def count_char_x(word, x):
  character_count = 0
  for letter in word:
    if letter == x:
      character_count += 1
  return character_count
  
print(count_char_x("mississippi", "s"))

print(count_char_x("mississippi", "m"))


#3. Check Name

def check_for_name(sentence, name):
  return name.lower() in sentence.lower()


#4 Every other letter

def every_other_letter(word):
  other_letter = ""
  for letter in range(0, len(word), 2):
    other_letter += word[letter]
  return other_letter


#5 Word length dict

def word_length_dictionary(words):
  word_length = {}
  for word in words:
    new_key = word
    new_value = len(new_key)
    word_length.update({new_key: new_value})
  return word_length
  
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

