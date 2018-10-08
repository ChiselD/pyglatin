# THINGS TO FIX
# 1. multiple consonants at start of word - DONE!
# 2. printing on separate lines - DONE!
# 3. non-alphabetical strings
# 3a. if user includes numbers, return error - DONE!
# 3b. if user includes punctuation, move it to correct location
# 4. omitted capitalization

# separate variables for the two possible endings
ay = 'ay'
yay = 'yay'

# create list to hold words of sentence in order
sentence = []

# reference list that tracks all vowels
vowels = ['a','e','i','o','u','y']

# function to run on words starting with vowels
def vowel(word):
	vowel_word = word + yay
	sentence.append(vowel_word)

# function to run on words starting with consonants
def consonant(word, first):
	# this variable will hold all letters before first vowel
	first_chunk = ''
	# I don't think there are any words in English that start with 'y' + another consonant (?)
	if first == 'y':
		first_chunk = first
	elif word[0] == 'q' and word[1] == 'u':
		first_chunk = 'qu'
	else:
		for letter in word:
			# look at each letter in word to see if it is a vowel
			if letter not in vowels:
				# as long as it's not, add it onto the end of the 'first_chunk' variable
				first_chunk += letter
			else:
				# as soon as you reach the first vowel in the word, break the loop
				break
	# consonant_word = all letters from first vowel to end + all letters before that + ay
	consonant_word = word[len(first_chunk):len(word)] + first_chunk + ay
	sentence.append(consonant_word)

# function to check if user input contains any digits
def has_number(input):
	# returns True if the string contains a digit
	return any(char.isdigit() for char in input)

# function to turn the user input into its Pig Latin equivalent
def pig_latinize_string(input):
	# lowercase user-entered string for practical purposes
	text = input.lower()
	# split original text into array of separate words
	words = text.split()
	# check each word: is it vowel-category or consonant-category?
	for word in words:
		# make variable to hold first letter only
		first = word[0]
		# if first letter is vowel, run vowel function
		if first in vowels and first != 'y':
			vowel(word)
		# if first letter is consonant, run consonant function
		else:
			consonant(word, first)

	# print each word in final 'sentence' list
	for item in sentence:
		print item,

# function that runs all the other functions (ALL HAIL MASTER FUNCTION)
def main():
	# reset sentence list to empty
	sentence = []

	# prompt user for text to Pig-Latinize
	original = raw_input("Enter your text: ")

	# confirm that user-entered string is not empty
	if len(original) > 0:
		# if string contains numbers, refuse it and re-prompt
		if has_number(original):
			print "Please enter a string that contains only letters and punctuation."
			main()
		# otherwise, let's DO this thing
		else:
			pig_latinize_string(original)
	else:
		# if user-entered string is empty, throw error and re-prompt
		print "No input!"
		main()

main()
