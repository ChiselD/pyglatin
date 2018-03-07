# two categories of words: starting with vowels and starting with consonants

# create separate variable for ending
ay = "ay"
yay = "yay"

# prompt user for text
original = raw_input("Enter your text: ")

# check if string is not empty and is purely alphabetical
if len(original) > 0 and original.isalpha():
	# lowercase it
	text = original.lower()
	# split original text into array of separate words
	words = original.split()
	# check each word: is it vowel-category or consonant-category?
	for word in words:
		# make variable to hold first letter only
		first = word[0]
		# check if first letter is vowel
		if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
			print "word begins with vowel!"
		else:
			print "word begins with consonant!"

	# PL-ized word = all-but-first of original + first of original + 'ay'
	# new_word = word[1:len(word)] + first + ay
	# print new_word

else:
	print 'empty'

#def vowel():
#def consonant():

