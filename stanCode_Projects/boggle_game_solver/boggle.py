"""
File: boggle.py
Name: Shih Hsuan Lin
----------------------------------------
This program will find the boggle from the letter board.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	This program will find the boggle from the letter board.
	"""
	row_1 = input('1 row of letters: ').lower()
	if not is_legal_string(row_1):
		return
	row_2 = input('2 row of letters: ').lower()
	if not is_legal_string(row_2):
		return
	row_3 = input('3 row of letters: ').lower()
	if not is_legal_string(row_3):
		return
	row_4 = input('4 row of letters: ').lower()
	if not is_legal_string(row_4):
		return
	start = time.time()

	# Build the letter board using dict
	letter_board = {}
	y_coordinate = 0
	for y in row_1, row_2, row_3, row_4:
		x_coordinate = 0
		for x in y.split(' '):
			letter_board[x_coordinate, y_coordinate] = x
			x_coordinate += 1
		y_coordinate += 1

	# Read the word set
	word_set = read_dictionary(''.join(row_1.split(' '))+''.join(row_2.split(' '))+''.join(row_3.split(' '))+''.join(row_4.split(' ')))

	number_of_words = [0]
	for y in range(4):
		for x in range(4):
			current_coordinate = (x, y)
			boggle(letter_board, letter_board[current_coordinate], number_of_words, word_set, current_coordinate, [current_coordinate])
	print(f'There are {number_of_words[0]} words in total.')
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def boggle(letter_board, current_s, number_of_words, word_set, current_coordinate, visited_coordinates):
	"""
	:param letter_board: dict, the input 16 letters
	:param current_s: str, current string
	:param number_of_words: list, the list of one int, record the number of words
	:param word_set: set, the dictionary of words
	:param current_coordinate: tuple, the current coordinate of this recursive function
	:param visited_coordinates: list, a list of tuple, record tje visited coordinate
	:return: None
	"""
	if current_s in word_set:
		print(f'Found "{current_s}"')
		number_of_words[0] += 1
		word_set.remove(current_s)
	for i in range(-1, 2):
		for j in range(-1, 2):
			next_coordinate = current_coordinate[0]+i, current_coordinate[1]+j
			if next_coordinate in letter_board and next_coordinate not in visited_coordinates:
				new_s = current_s+letter_board[next_coordinate]
				if has_prefix(new_s, word_set):
					visited_coordinates.append(next_coordinate)
					boggle(letter_board, new_s, number_of_words, word_set, next_coordinate, visited_coordinates)
					visited_coordinates.pop()


def is_legal_string(string):
	"""
	:param string: str, the input string
	:return: bool, whether the input string is legal
	"""
	if len(string) != 7:
		print('Illegal input')
		return False
	for i in range(len(string)):
		if i % 2 == 0:
			if not string[i].isalpha():
				print('Illegal input')
				return False
		else:
			if string[i] != ' ':
				print('Illegal input')
				return False
	return True


def read_dictionary(letters):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	word_set = set()
	with open(FILE, 'r') as f:
		for line in f:
			if len(line) > 4 and word_check(line, letters):
				word = line.strip()
				word_set.add(word)
	return word_set


def word_check(word, letters):
	"""
	:param word: str, the word in dictionary
	:param letters: str, the input 16 letters
	:return: bool, whether the word is possible
	"""
	for letter in letters:
		if word.count(letter) > letters.count(letter):
			return False
	return True


def has_prefix(sub_s, word_set):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in word_set:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
