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

#6 frequency counts

def frequency_dictionary(words):
  frequency = {}
  for word in words:
    if word not in frequency:
      frequency[word] = 0
    frequency [word] += 1
  return frequency

print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}


#Unique values

def unique_values(my_dictionary):
  unique_values = []
  for value in my_dictionary.values():
    if value not in unique_values:
      unique_values.append(value)
  return len(unique_values)

print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

#count first letter

def count_first_letter(names):
  letters = {}
  for key in names.keys():
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters
  
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}