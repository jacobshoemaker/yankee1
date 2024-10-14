# Don't forget to run the tests (and create some of your own)

# Part 1
def is_character_match(string1, string2):
	# Converting both strings into lists of lowercased characters
	string1_list_LC = list(string1.lower())
	string2_list_LC = list(string2.lower())
 
	# Creating an empty list that will be populated with each 
	# matching character
	letter_match_list = []
	
	# Iterating through string1_list_LC and appending each character
	# to letter_match_list
	# that is matched in string2_list_LC
	for letter in string1_list_LC:
		if letter in string2_list_LC:
			letter_match_list.append(letter)
	# If neither string1 list or string2 list is the same
	# as letter_match_list, return False. Else, return True
	if ((letter_match_list != string1_list_LC) and (letter_match_list != string2_list_LC)):
		return False
	else:
		return True
# Part 2
def anagrams_for(word, list_of_words):
	# Converting word to list of characters
	anagram_list = []
	# Sorting word in alphabetical order and storing into sorted_word variable
	sorted_word = sorted(word.lower())
	
	# Iterating through list_of_words
	for element in list_of_words:
    # If sorted_word is the same as the sorted element in list_of_words,
    # Append that element to anagram_list
		if sorted_word == sorted(element.lower()):
			anagram_list.append(element)
	return anagram_list


				