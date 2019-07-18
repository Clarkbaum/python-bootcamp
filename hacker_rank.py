# https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(string):
	vowels = "AEIOU"

	sample_length = 0
	stuart_points = 0
	kevin_points = 0
	string_vowles = []
	string_consonants = []

	for char in string:
		if char in vowels:
			if char not in string_vowles:
				string_vowles.append(char)
		else:
			if char not in string_consonants:
				string_consonants.append(char)

	for sample_length in range(1, len(string) + 1):
		for vowel in string_vowles:
			junk1 = string.index(vowel)
			junk2 = string[string.index(vowel) : string.index(vowel) + sample_length]
			junk3 = occurrences(string, string[string.index(vowel) : string.index(vowel) + sample_length])
			junk4 = string.index(vowel) + sample_length
			junk5 = len(string)
			kevin_points += occurrences(string, string[string.index(vowel) : string.index(vowel) + sample_length])

			if string.index(vowel) + sample_length >= len(string):
				string_vowles.remove(vowel)

		for consonant in string_consonants:
			
			if string.index(consonant) + sample_length >= len(string):
				string_consonants.remove(consonant)
			stuart_points += occurrences(string, string[string.index(consonant) : string.index(consonant) + sample_length])

	print("string_vowles: ", string_vowles)
	print("string_consonants", string_consonants)

	
	print("stuart_points: ", stuart_points)
	print("kevin_points: ", kevin_points)

	if stuart_points > kevin_points:
		print(f"Stuart {stuart_points}")
	else:
		print(f"Kevin {kevin_points}")

def occurrences(string, sub):
	count = start = 0
	while True:
		start = string.find(sub, start) + 1
		if start > 0:
			count+=1
		else:
			return count

minion_game("BANANA")