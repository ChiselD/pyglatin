# two categories of words: starting with vowels and starting with consonants

# create separate variable for ending
ay = "ay"
yay = "yay"

# prompt user for text
original = raw_input("Enter your text: ")

words = original.split()

print words
print words[1]

#def vowel():
#def consonant():

# check if string is not empty and is purely alphabetical
if len(original) > 0 and original.isalpha():
  # lowercase it
  word = original.lower()
  # make variable to hold first letter only
  first = word[0]
  # PL-ized word = all-but-first of original + first of original + 'ay'
  new_word = word[1:len(word)] + first + ay
  print new_word
else:
  print 'empty'