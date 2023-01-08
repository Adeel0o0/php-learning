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