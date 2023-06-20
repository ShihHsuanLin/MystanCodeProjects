"""
File: anagram.py
Name: Shih Hsuan Lin
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    Input any word to find anagrams in dictionary.txt
    """
    print(f'Welcome to stanCode "Anagram Generator" (or {EXIT} to quit)')
    while True:
        s = input('Find anagrams for: ')
        start = time.time()
        if s == EXIT:
            break
        print('Searching...')
        anagrams = find_anagrams(s)
        print(f'{len(anagrams)} anagrams: {anagrams}')
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(sorted_s):
    word_set = set()
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()
            if len(word) == len(sorted_s) and ''.join(sorted(word)) == sorted_s:
                word_set.add(word)
    return word_set


def find_anagrams(s):
    """
    :param s: str, the input word
    :return: list, the anagrams list of the input word
    """
    word_set = read_dictionary(''.join(sorted(s)))
    return find_anagrams_helper(s, '', [], word_set)


def find_anagrams_helper(s, current_s, anagrams_lst, word_set):
    """
    :param s: str, the input word
    :param current_s: str, the current string in this recursive function
    :param anagrams_lst: list, the current anagrams list of the input word
    :param word_set: set, the set of word dictionary
    :return: list, the anagrams list of the input word
    """
    if len(s) == 0:
        if current_s not in anagrams_lst:
            print(f'Found: {current_s}\nSearching...')
            anagrams_lst.append(current_s)
            word_set.remove(current_s)
    else:
        for i in range(len(s)):
            letter = s[i]
            if has_prefix(current_s+letter, word_set):
                find_anagrams_helper(s[:i]+s[i+1:], current_s+letter, anagrams_lst, word_set)
    return anagrams_lst


def has_prefix(sub_s, word_set):
    """
    :param sub_s: str, this string will be checked if it is the beginning of a word in the word_set
    :param word_set: set, the set of word dictionary
    :return: boolean, the boolean indicating whether sub_s is the beginning of a word in the word_set
    """
    for word in word_set:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
