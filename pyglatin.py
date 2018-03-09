# THINGS TO FIX
# 0. add README
# 1. multiple consonants at start of word
# 2. non-alphabetical strings

# create separate variable for ending
ay = "ay"
yay = "yay"

# define function to run on words starting with vowels
def vowel(x):
	vowel_word = x + yay
	print vowel_word

# define function to run on words starting with consonants
def consonant(y, z):
	consonant_word = y[1:len(y)] + z + ay
	print consonant_word

# prompt user for text
original = raw_input("Enter your text: ")

# check if string is not empty
if len(original) > 0:
	# lowercase it
	text = original.lower()
	# split original text into array of separate words
	words = text.split()
	# check each word: is it vowel-category or consonant-category?
	for word in words:
		# make variable to hold first letter only
		first = word[0]
		# check if first letter is vowel
		if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
			vowel(word)
		else:
			consonant(word, first)

	# PL-ized word = all-but-first of original + first of original + 'ay'
	# new_word = word[1:len(word)] + first + ay
	# print new_word

else:
	print 'empty'

