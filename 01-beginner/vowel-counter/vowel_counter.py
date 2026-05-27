word = input('Enter Word ')

vowels_list = 'aeiouAEIOU'

vowels = []
consonants = []

for letter in word:
	if letter in vowels_list:
		vowels.append(letter)
	else:
		consonants.append(letter)

vowel_count = len(vowels)

print('Vowels : ', vowels)
print('Consonants : ', consonants)
print('Total number of vowels : ', vowel_count)