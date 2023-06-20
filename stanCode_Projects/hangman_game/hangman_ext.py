"""
File: hangman.py
Name: Shih Hsuan Lin
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program plays hangman game.
    Users sees a dashed word, trying to
    correctly figure the un-dashed word out
    by inputting one character each round.
    If the user input is correct, show the
    updated word on console. Players have N_TURNS
    chances to try and win this game.
    """
    answer = random_word()
    dashed = ''
    for i in range(len(answer)):
        dashed += '-'
    n_turns = N_TURNS
    while True:
        print('The word looks like '+dashed+'\nYou have '+str(n_turns)+' wrong guesses left.')
        input_ch = input('Your guess: ')
        input_ch = format_check(input_ch).upper()
        if input_ch in answer:
            print('You are correct!')
            dashed = refresh_dashed(dashed, input_ch, answer)
        else:
            plot(n_turns)
            print('There is no '+input_ch+"'s in the word.")
            n_turns -= 1
        if "-" not in dashed:
            print('You win!!\nThe word was: '+answer)
            break
        elif n_turns == 0:
            print('You are completely hung : (\nThe word was: '+answer)
            break


def format_check(input_ch):
    """
    :param input_ch: str, any string
    :return: str, single alphabet
    """
    while True:
        if input_ch.isalpha():
            if len(input_ch) == 1:
                break
        input_ch = input('Illegal format.\nYour guess: ')
    return input_ch


def refresh_dashed(dashed, input_ch, answer):
    """
    :param dashed: str, old dashed
    :param input_ch: str
    :param answer: str
    :return: str, new dashed
    """
    ans = ''
    for i in range(len(answer)):
        ch = answer[i]
        if ch == input_ch:
            ans += ch
        else:
            ans += dashed[i]
    return ans


def plot(n_turns):
    """
    :param n_turns: int
    """
    if n_turns == 7:
        print(' |--------\n'
              ' |      |\n'
              ' |      |\n'
              ' |\n'
              ' |\n'
              ' |\n'
              ' |\n'
              '-|----------------')
    elif n_turns == 6:
        print(' |--------\n'
              ' |      |\n'
              ' |      |\n'
              ' |      **\n'
              ' |      **\n'
              ' |\n'
              ' |\n'
              '-|----------------')
    elif n_turns == 5:
        print(' |--------\n'
              ' |      |\n'
              ' |      |\n'
              ' |      **\n'
              ' |      **\n'
              ' |      |\n'
              ' |\n'
              '-|----------------')
    elif n_turns == 4:
        print(' |--------\n'
              ' |      |\n'
              ' |      |\n'
              ' |      **\n'
              ' |      **\n'
              ' |      |\\\n'
              ' |\n'
              '-|----------------')
    elif n_turns == 3:
        print(' |--------\n'
              ' |      |\n'
              ' |      |\n'
              ' |      **\n'
              ' |      **\n'
              ' |     /|\\\n'
              ' |\n'
              '-|----------------')
    elif n_turns == 2:
        print(' |--------\n'
              ' |      |\n'
              ' |      |\n'
              ' |      **\n'
              ' |      **\n'
              ' |     /|\\\n'
              ' |     /\n'
              '-|----------------')
    elif n_turns == 1:
        print(' |--------\n'
              ' |      |\n'
              ' |      |\n'
              ' |      **\n'
              ' |      **\n'
              ' |     /|\\\n'
              ' |     / \\\n'
              '-|----------------')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
