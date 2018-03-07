# create separate variable for ending
pyg = 'ay'

# prompt user for word. TODO: change to full phrase
original = raw_input('Enter a word: ')

# check if string is not empty and is purely alphabetical
if len(original) > 0 and original.isalpha():
  # lowercase it
  word = original.lower()
  # make variable to hold first letter only
  first = word[0]
  # PL-ized word = all-but-first of original + first of original + 'ay'
  new_word = word[1:len(word)] + first + pyg
  print new_word
else:
  print 'empty'