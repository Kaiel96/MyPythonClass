
word = 'Hello class!'

for letter in word:
   print letter

for spot in range (len(word)): 
   print word[spot]

#strings are immutable 

new_word = word + '!'

def count_vowels(word):
	count = 0
	for letter in word: 
		if letter in 'aeiouAEIOU': 
			return count += 1
	return count 

def has_vowel(word):
	for letter in word: 
		if letter in 'aeiouAEIOU': 
			return True
	return False
